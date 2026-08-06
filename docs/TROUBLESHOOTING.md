# Troubleshooting

## SSL Certificate Verification Error (Corporate/Jamf-managed Mac)

### Issue
Running scripts that make HTTPS requests (e.g. `python test.py` calling the
Tavily API) fails with:

```
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1000)
...
requests.exceptions.SSLError: HTTPSConnectionPool(host='api.tavily.com', port=443): Max retries exceeded with url: /search (Caused by SSLError(SSLCertVerificationError(...)))
```

### Cause
Corporate/office networks (managed via Jamf/MDM) often route outbound HTTPS
traffic through a proxy that performs TLS inspection (MITM). The proxy
presents its own root CA certificate, which is trusted by the macOS system
Keychain (installed via MDM profile) but **not** by Python's bundled
`certifi` CA store. Since `requests`/`urllib3` (used internally by the
`tavily` SDK) verify certificates against `certifi` by default, the
connection fails even though the same traffic works fine in a browser or via
`pip install` (which may go through an already-authorized internal proxy
like AWS CodeArtifact).

### Solution
Install `pip-system-certs`, which patches Python's `ssl`/`urllib3` to use the
macOS system trust store (Keychain) instead of `certifi`'s bundled CAs:

```bash
source .venv/bin/activate
pip install pip-system-certs --index-url https://pypi.org/simple/
```

After installation, no code changes are required — `pip-system-certs`
patches SSL verification globally for the active Python environment. Re-run
your script:

```bash
python test.py
```

### Notes
- This fix must be applied per virtual environment (`.venv`), since
  `pip-system-certs` patches the environment it's installed into.
- If you recreate the `.venv`, reinstall `pip-system-certs`.
- Prefer `--index-url https://pypi.org/simple/` when installing packages not
  available in the corporate private PyPI index (e.g. AWS CodeArtifact).
