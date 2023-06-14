import requests
from bs4 import BeautifulSoup
import time

keyword = "감자"
pages = 3
title_list = []

def collect_list(keyword, start):
  url = url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query="+keyword+"&sort=1&photo=0&field=0&pd=3&ds=2021.02.01&de=2021.05.31&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:dd,p:from20210201to20210531,a:all&start="+str(start)
  response = requests.get(url)
  soup = BeautifulSoup(response.text, "html.parser")
  links = soup.find_all("a", class_="news_tit")
  
  for i, link in enumerate(links):
    title = link.text
    url = link["href"]
    title_list.append([start + i, title, url])
    print(start + i, title, url)

for page in range(pages):
  start = page * 10 + 1
  collect_list(keyword, start)
  time.sleep(6)