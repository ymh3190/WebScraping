import requests
from bs4 import BeautifulSoup

RECRUITPAGE = 1
URL = f"http://www.saramin.co.kr/zf_user/search/recruit?searchword=python&recruitPageCount=100&recruitPage="

#1. 페이지를 가져올 것
#2. requests를 만들 것
#3. jobs 추출하기

def get_last_page():
    result = requests.get(f"{URL}{RECRUITPAGE}")
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class": "pagination"})
    links = pagination.find_all('a')
    pages = [link.find("span").string for link in links[:-1]]
    max_page = int(pages[-1])
    result = requests.get(f"{URL}{max_page+1}")
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class": "pagination"})
    links = pagination.find_all('a')
    pages = [link.find("span").string for link in links[1:]]
    max_page = int(pages[-1])
    return max_page

def extract_job(html, value):
    title = html.find("h2", {"class": "job_tit"}).find('a')["title"]
    company = html.find("strong", {"class": "corp_name"}).find('a')["title"]
    job_condition = html.find("div", {"class": "job_condition"}).find("span").find_all('a')
    job_id = value.find_all("div", {"class": "value"})
    print(job_condition[0].string)
    return {
        'title': title,
        'company': company,
        'location': f"{job_condition[0].string}",
        'link': f"http://www.saramin.co.kr/zf_user/jobs/relay/view?isMypage=no&rec_idx={job_id}"
    }

def extract_jobs(last_page):
    jobs = []
    for page in range(1, last_page+1):
        # print(f"Scrapping page {page}")
        result = requests.get(f"{URL}{RECRUITPAGE*page}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "item_recruit"})
        value = soup.find("div", {"class": "content"})
        for result in results:
            jobs.append(extract_job(result, value))
    return jobs

def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs

