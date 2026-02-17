import requests
from bs4 import BeautifulSoup

url="https://umei.net/year/"

headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0"

}

data={

}
def crawl_picture():

    respon=requests.get(url=url,headers=headers,data=data)
    print(respon.url)

if __name__ == "__main__":
    crawl_picture()