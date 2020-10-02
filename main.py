#1. 먼저 url로 접근하기
#2. 검색 설정으로 가서 페이지당 검색결과 수를 50으로 늘린다.
#3. 이렇게해서 나온 url을 이용한다. ex) https://kr.indeed.com/jobs?q=python&limit=50
#4. import urllib

#5 requests
"""
import urllib3보다 더 좋은 패키지가 있다.
requests : 파이썬에서 요청을 만드는 기능을 모아 놓은 것
사용법은 python requests !g 구글링해서 github 주소로 이동하고, README.md 참고
"""

#6. requests 설치
#import requests

#indeed_result=requests.get("https://kr.indeed.com/jobs?q=python&limit=50")

#print(indeed_result) #[200]이라고 뜨면 정상
#print(indeed_result.text) # text 추출. json(), encoding, headers도 가져올 수 있다.

"""
파이썬만(urllib) 사용해서 urls를 가져올 수 있었나? - YES
그러나 온라인에 있는 라이브러리(requests)를 통해서 더 강력한 기능을 사용할 수 있지
"""

#7.beautifulsoup4 설치 : html에서 정보를 추출하는 유용한 패키지
"""
cf) https://www.crummy.com/software/BeautifulSoup/bs4/doc/
1. Quick Start
html_doc -> 이미 print(indeed_result.text)로 가져왔다.

2. from bs4 import BeautifulSoup

"""
#from bs4 import BeautifulSoup

#indeed_soup = BeautifulSoup(indeed_result.text, "html.parser") #페이지가 총 몇개인지 보는 것

#print(indeed_soup)

"""
3. find_all('a') 사용
첫 페이지의 html을 볼껀데, inspect(F12)로 들어가서 pagination을 찾는다.
이제 class명이 pagination을인 div를 찾도록 하자.
"""
#pagination = indeed_soup.find("div", {"class":"pagination"}) #페이지에서 div와 class:pagination을 찾는다.

#print(pagination)

#links = pagination.find_all('a') #모든 링크의 리스트를 반환한다.

#print(links)

"""
4. a안의 모든 apan가져오기
나중에 function을 만들건데 가장 높은 숫자를 찾을 거야
"""
#for link in links:
#    print(link.find("span")) #마지막줄은 next라는 값

"""
5. 마지막에 출력된 걸 없애줘야돼
"""
#spans=[]
#for link in links:
#    spans.append(link.find("span"))
#print(spans)

#위의 3줄은 굉장히 많이 사용되는 코드이기에 사람들이 1줄로 많듬
#pages = [links[i].find("span") for i in range(len(links))] #찾은 링크에서 span(페이지넘버)만 가지고 오는 것이 목적
#print(pages[:-1]) #마지막 줄은 제외하고 출력

"""
6. 타이틀 텍스트만 가져오기
"""
#pages = [link.find("span").string for link in links]
#pages = pages[:-1]
#print(pages)

"""
7. span에 있는 string이 아니라 대신 링크 안에 string을 가져오면 어떻게 될까?
링크는 a(anchor)였다.
"""
#pages = [link.string for link in links)]
#pages = pages[:-1]
#print(pages)

"""
8. 링크안의 string을 int로 형변환
int() 혹은 map(int,)
"""
#pages = [int(link.string) for link in links[:-1]]
#pages = list(map(int, pages))
#print(pages[-1])
#max_page=pages[-1]

#pages=[]
#for link in links[:-1]:
#    pages.append(int(link.string))
#print(pages)

"""
9. request를 수작업으로 여러 개 만들기 
"""
#pages = [int(link.string) for link in links[:-1]]
#max_page=pages[-1]

#for n in range(max_page):
#    print(f"start={n*50}")
    #원한다면 이대로 코드를 추가할 수 있지만 너무 지저분해지니까 함수를 만들자.

"""
10. 최대 페이지 수를 불러오는 모듈 임포트
"""
# from indeed import extract_indeed_pages, extract_indeed_jobs

# max_indeed_pages = extract_indeed_pages()

#print(max_indeed_pages)

"""
11. 이제 또 다른 함수를 만들어 보자
indeed_pages을 입력으로 받아서 페이지 수만큼 요청하기
"""
#from indeed import extract_indeed_jobs

# last_indeed_page = extract_indeed_pages()

#extract_indeed_jobs(last_indeed_page)

"""
12. 각 페이지로 가서 일자리 정보를 추출한 정보를 담고 모든 일자리를 반환하기
어떻게 데이터를 html에서 추출해야할까? -> soup을 사용하면 돼
1) 타이틀 가져오기
2) 회사이름 가져오기
3) 회사주소 가져오기
4) 회사 링크 가져오기
"""

"""
13. indeed.py파일에서 아래의 코드를 대신할 함수 만들기
last_indeed_page = extract_indeed_pages()
indeed_jobs = extract_indeed_jobs(last_indeed_page)
"""
# from indeed import get_jobs as get_indeed_jobs

# indeed_jobs = get_indeed_jobs()

# print(indeed_jobs)

"""
14. 다른 채용사이트(사람인)에서 같은 작업하기
"""
from indeed import get_jobs as get_indeed_jobs
from so import get_jobs as get_so_jobs
from save import save_to_file

indeed_jobs = get_indeed_jobs()
so_jobs = get_so_jobs()
jobs = indeed_jobs
save_to_file(jobs)
