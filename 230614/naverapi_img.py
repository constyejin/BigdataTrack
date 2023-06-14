# from requests import get
# import requests시 response에서 requests.get 으로 작성
import requests
import time
import os
import json
import pandas as pd

client_id = "O0sl9zVJg2m8bw809A3v"
client_pw = "WAaH_SJDwf"
query = "청바지"

def get_img(i, url):
  user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
  headers = {"User-Agent": user_agent}

  # 파일 확장자명
  file_ext = url.split(".")[-1]
  img = requests.get(url).content
  open('/images/+'+str(i)+"."+file_ext,'wb').write(img)


# 이미지 수집하는 메인 함수
def get_list(query):
  print(query)
  user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
  headers = {"User-Agent": user_agent,
             "X-Naver-Client-Id": client_id,
             "X-Naver-Client-Secret": client_pw
             }

  url = "https://openapi.naver.com/v1/search/image?query=" + query
  print(url)

  response = requests.get(url, headers=headers)
  print(response.text)
  elements = json.loads(response.text)['items']

  for i, elm in enumerate(elements):
    title = elm['title']
    link = elm['link']
    thumbnail = elm['thumbnail']
    sizewidth = elm['sizewidth']
    sizeheight = elm['sizeheight']
    img_list.append([title, link, thumbnail, sizewidth, sizeheight])
    print([title, link, thumbnail, sizewidth, sizeheight])

    get_img(i, link)

  return img_list

img_list = []
img_list =  get_list(query)


df = pd.DataFrame(img_list, columns=['title', 'link', 'thumbnail', 'sizewidth', 'sizeheight'])
df.to_csv('img_list.csv', index=False)

get_list(query)