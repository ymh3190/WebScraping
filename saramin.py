import requests
from bs4 import BeautifulSoup

RECRUITPAGE = 1
URL = f"http://www.saramin.co.kr/zf_user/search/recruit?searchword=python&recruitPage={RECRUITPAGE}&recruitPageCount=100"

#1. 페이지를 가져올 것
#2. requests를 만들 것
#3. jobs 추출하기

def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class": "pagination"})
    links = pagination.find_all('a')
    pages = [link.find("span").string for link in links[:-1]]
    max_page = int(pages[-1])
    print(max_page)

def get_jobs():
    last_page = get_last_page()
    return []

