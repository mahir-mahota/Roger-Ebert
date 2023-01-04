from bs4 import BeautifulSoup
import requests

def get_results(query):
    request = requests.get(query)

    page_content = BeautifulSoup(request.content, 'html.parser')

    para = page_content.find_all('p')
    useful = []

    for p in para:
        if len(para) > 10 and len(p.text) > 200:
            useful.append(p.text)
        
    return useful
        
       