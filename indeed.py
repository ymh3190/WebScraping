import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages() :
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  pagination = soup.find("div", {"class":"pagination"})
  links = pagination.find_all('a')
  pages = [int(link.string) for link in links[:-1]]
  max_page = pages[-1]
  return max_page
#print(f"&start={page*LIMIT}")

def extract_job(html):
  title = html.find("h2", {"class": {"title"}}).find("a")["title"]
  # 회사이름에 링크가 있는게 있고 없는게 있다. -> if else
  company = html.find("span", {"class": "company"})
  company_anchor = company.find("a")
  if company_anchor is not None:
      company = str(company_anchor.string)
  else:
      company = str(company.string)
  company = company.strip()  # string.strip함수는 문자열 양끝에 있는 공백과 \n를 삭제한다.
  location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]
  job_id = html["data-jk"]
  return {
      'title': title,
      'company': company,
      'location': location,
      "link": f"https://kr.indeed.com/viewjob?jk={job_id}"
  }

def extract_indeed_jobs(last_page):
    results = None
    for page in range(last_page):
        print(f"Scrapping page {page}")
        result = requests.get(f"{URL}&start={page*LIMIT}")
    #print(results.status_code)
    # jobs = []
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
    #print(results)
    #for result in results:
        #title = result.find("h2", {"class": "title"}) #요소 변경으로 인해 div->h2
        #print(title)
        #print(title.find("a").string)
        #anchor = title.find("a")["title"]
        #print(anchor)
        # jobs = extract_job(result)
    jobs = [extract_job(result) for result in results]
    return jobs
