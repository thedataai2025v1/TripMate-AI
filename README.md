# TripMate-AI
python3 -m venv .venv
source .venv/bin/activate
pip install --index-url https://pypi.org/simple/ -r requirements.txt

pip install certifi
python test.py


pip install pip-system-certs --index-url https://pypi.org/simple/