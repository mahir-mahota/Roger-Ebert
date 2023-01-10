from bs4 import BeautifulSoup
import requests
from googlesearch import search
from random  import randint

def search_query(query):
    
    PAUSE = randint(1, 10)
    urls = search(query + " 'review'", stop = 10, start = 5, num = 10, lang = 'en', pause = PAUSE)

    results = []

    for url in urls:
        text = get_text(url)
        results.extend(text)

    print(results)
    return results


def get_text(url):

    headers = requests.utils.default_headers()

    headers.update({'User-Agent': 'My User Agent 1.0',})

    request = requests.get(url, allow_redirects = False, headers = headers)
    useful = []

    if request.status_code >= 200 and request.status_code < 300:

        page_content = BeautifulSoup(request.content, 'html.parser')

        para = page_content.find_all('p')

        for p in para:
            if len(para) > 10 and len(p.text) > 200:
                useful.append(p.text.strip())
        
    return useful