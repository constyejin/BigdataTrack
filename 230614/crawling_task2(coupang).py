import requests
from bs4 import BeautifulSoup

url = "https://www.coupang.com/vp/products/24092628?itemId=93814063&vendorItemId=3165942988&pickType=COU_PICK&q=%ED%82%A5%EB%B3%B4%EB%93%9C&itemsCount=36&searchId=292b03298ac64c47b241e30a440e611b&rank=1&isAddedCart="
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
links = soup.find_all("a", class_="descriptions-inner")
title_list = []

print(links)

# for i, link in enumerate(links):
#   title = link.text
#   url = link
#   title_list.append([i + 1, title, url])
#   print(i + 1, title, url) 