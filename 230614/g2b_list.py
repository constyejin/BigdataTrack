import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
import time

keywords = ["배수지", "농어촌"]
output_file_name = "pjt_g2b_crawl.txt"
output_file = open(output_file_name, 'w', encoding='utf-8')
output_file.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format("keyword", "i", "bid_category", "bid_id", "bid_url", "bid_class", "bid_name", "bid_org", "need_org" ,"contact_type", "create_date", "modify_date"))
output_file.close()

def get_data(keyword):
    # utf-8은 생략 가능
    query = quote(keyword, encoding="euc-kr")
    url = "https://www.g2b.go.kr:8101/ep/tbid/tbidList.do?taskClCds=&bidNm=" + query + "&searchDtType=1&fromBidDt=2023/05/15&toBidDt=2023/06/14&fromOpenBidDt=&toOpenBidDt=&radOrgan=1&instNm=&area=&regYn=Y&bidSearchType=1&searchType=1"
    print(url)
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    re_tbody = soup.tbody
    re_trs = re_tbody.find_all("tr")
    print(len(re_trs))

    for i, re_tr in enumerate(re_trs):
        re_td = re_tr.find_all("td")
        bid_category = re_td[0].div.text
        bid_id = re_td[1].div.text.split('-')[0]
        bid_url = re_td[1].div.a.get("href")
        bid_class = re_td[2].div.text
        bid_name = re_td[3].div.text
        bid_org = re_td[4].div.text
        need_org = re_td[5].div.text
        contact_type = re_td[6].div.text
        create_date = re_td[7].div.text.split('.')[0]
        modify_date = re_td[7].div.text.split('(')[1].replace(')', '')
        

        print(keyword, i, bid_category, bid_id, bid_url, bid_class, bid_name, bid_org, need_org ,contact_type, create_date, modify_date)

        output_file = open(output_file_name, 'a', encoding='utf-8')
        output_file.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(keyword, str(i + 1).zfill(2), bid_category, bid_id, bid_url, bid_class, bid_name, bid_org, need_org ,contact_type, create_date, modify_date))
        output_file.close()

def main():
  for keyword in keywords:
     get_data(keyword)
     time.sleep(6)

main()