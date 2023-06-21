from requests import get
import time
import os
import json
from html import unescape

client_id = "O0sl9zVJg2m8bw809A3v"
clinet_pw = "WAaH_SJDwf"
queries = ["서평 세이노의 가르침", "서평 역행자"]
max_start = 2

file_name = "naver_kin.txt"
file = open(file_name, 'w')
file.write('{}\t{}\t{}\t{}\t{}\t{}\n'.format('query', 'no', 'title', 'link', 'description', 'total_text'))
file.close()

def get_list(query, start):
  print(query)
  user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
  headers = {"User-Agent": user_agent,
             "X-Naver-Client-Id": client_id,
             "X-Naver-Client-Secret": clinet_pw,
             }
  url = "https://openapi.naver.com/v1/search/kin.json?query=" + query + "&display=100&start=" + str(start + 1) + "&sort=sim"
  print(url)

  response = get(url, headers=headers)
  # print(response.text)
  elemnets = json.loads(response.text)['items']

  for i, elm in enumerate(elemnets):
    title = elm['title'].replace("<b>", "").replace("</b>", "")
    title = unescape(title)

    link = elm['link']
    
    description = elm['title'].replace("<b>", "").replace("</b>", "")
    description = unescape(title)

    total_text = title + "  " + description

    print([query, (start *100) + (i + 1), title, link, description, total_text])
    file = open(file_name, 'a')
    file.write('{}\t{}\t{}\t{}\t{}\t{}\n'.format(query, (start *100) + (i + 1), title, link, description, total_text))
    file.close()

  return

for query in queries:
  for start in range(max_start):
    get_list(query, start)
    time.sleep(0.5)
