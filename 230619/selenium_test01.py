from selenium.webdriver.common.by import By
from selenium import webdriver
import time


driver = webdriver.Chrome()

url = "https://news.naver.com"
driver.switch_to.window(driver.window_handles[0])
driver.get(url)

driver.find_element(By.CLASS_NAME, "Nicon_search").click()
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, "input[type='search']").send_keys("빅데이터")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(1)

# New tap
driver.switch_to.window(driver.window_handles[1])
time.sleep(1)
driver.find_elements(By.CSS_SELECTOR, "a[class='item']")[1].click()

bodies = driver.find_elements(By.CSS_SELECTOR, "li[class='bx']")

news_list = []
for body in bodies:
    title = body.find_element(By.CSS_SELECTOR, "a[class='news_tit']").text
    link = body.find_element(By.CSS_SELECTOR, "a[class='news_tit']").get_attribute("href")
    news_list.append([title, link])
    print([title, link])

pre_pagenation = driver.find_element(By.CSS_SELECTOR, "div[class='sc_page_inner']")
next_pagenation = pre_pagenation.find_element(By.LINK_TEXT, "2").click()

# "div[class='sc_page_inner']"를 list로 담아서 반복문
while(True):
    pass