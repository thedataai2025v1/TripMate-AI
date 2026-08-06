from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

client = TavilyClient(os.getenv("TAVILY_API_KEY"))

def tavily_search(query: str):
    response= client.search(query= query, max_results=5)
    results = []
    for i,r in enumerate(response["results"]):
        title = r.get("title","Unknown")
        url = r.get("url","")
        content = r.get("content","").strip()
        if len(content) > 300:
            content = content[:300].rsplit('.', 1)[0] + "..."
        
        results.append(f"{i+1}. **{title}**\n {url}\n{content}")
    return "\n\n".join(results)
