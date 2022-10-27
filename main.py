from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

def webParse(url):
        
    Headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }

    r = requests.get(url, headers=Headers)
    soup = BeautifulSoup(r.text, "html.parser")

    return soup

def getResult(uuid):

    web = webParse(f'https://www.koreaminecraft.net/?act=&vid=&mid=bmlist&category=&extra_vars1=&extra_vars2={uuid}')
    board = web.find_all(attrs={'class': 'title-link'})
    for a in board:
        if a.span == None:
            return a.text

app = FastAPI()

@app.get("/bmlist")
def test_index(uuid: str = None):
    title = getResult(uuid)
    if title:
        return {
            "isFind": True,
            "title": title
        }

    else:
        uuid = uuid.replace("-", "")
        title = getResult(uuid)
        if title:
            return {
                "isFind": True,
                "title": title
            }
        else:
            return {
                "isFind": False
            }
