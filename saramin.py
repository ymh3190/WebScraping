import requests
from bs4 import BeautifulSoup

URL = f"http://www.saramin.co.kr/zf_user/search/recruit?searchword=python&recruitPageCount=100&recruitPage="

def get_last_page():
    result = requests.get(f"{URL}{11}")
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "pagination"}).find_all("span")
    last_page = int(pages[-1].string)
    return last_page

def extract_job(html):
    title = html.find("h2").find("a")["title"]
    company = html.find("strong").find("a")["title"]
    location = html.find("div", {"class", "job_condition"}).find("span")
    location_anchor = location.find('a')
    if location_anchor is not None:
        location = location_anchor.string
    else:
        location = location.string
    rec_idx = html.find("div", {"class": "toolTipWrap wrap_scrap"}).find('a')["rec_idx"]
    return {
        "title": title,
        "company": company,
        "location": location,
        "link": f"http://www.saramin.co.kr/zf_user/jobs/relay/view?isMypage=no&rec_idx={rec_idx}"
    }

def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scraping Saramin: Page {page}")
        result = requests.get(f"{URL}{page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "item_recruit"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs

def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs
