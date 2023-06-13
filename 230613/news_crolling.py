import requests
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EB%B9%85%EB%8D%B0%EC%9D%B4%ED%84%B0&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=25&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start=21"
response = requests.get(url)

response.text
soup = BeautifulSoup(response.text, "html.parser")

title_list = []
links = soup.find_all("a", class_="news_tit")

# print(type(links))
# print(links)

# enumerate : 일련 번호 자동 생성 후 할당
for i, link in enumerate(links):
  title = link.text
  url = link["href"]
  title_list.append([i, title, url])
  print(i, title, url)

  # list append()와 extend() 차이점
  # 1. append()
  # append는 덧붙인다는 뜻으로 괄호( ) 안에 값을 입력하면 새로운 요소를 array 맨 끝에 객체로 추가한다.
  # 2. extend()
  # iterable의 각 요소를 하나씩 array의 끝에 요소로 추가한다. append 함수와 다른 점은 괄호 안에 iterable 자료형만 올 수 있다.