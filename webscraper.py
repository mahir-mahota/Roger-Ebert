from bs4 import BeautifulSoup
import requests
from googlesearch import search

async def search_query(query):
    
    urls = search(query, start = 5, num = 10, lang = 'en', pause = 10)
    results = []

    for url in urls:
        text = await get_text(url)
        results.extend(text)
    print(results)
    return results


async def get_text(url):

    request = requests.get(url)
    useful = []

    if request.status_code >= 200 and request.status_code < 300:

        page_content = BeautifulSoup(request.content, 'html.parser')

        para = page_content.find_all('p')

        for p in para:
            if len(para) > 10 and len(p.text) > 200:
                useful.append(p.text.strip())
        
    return useful