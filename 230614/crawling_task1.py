import requests
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EC%A0%90%EC%8B%AC&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=15&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start=11"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
title_list = []
links = soup.find_all("a", class_="news_tit")

for i, link in enumerate(links):
  title = link.text
  url = link["href"]
  title_list.append([i + 1, title, url])
  print(i + 1, title, url) 