from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "https://news.naver.com"
driver.switch_to.window(driver.window_handles[0])
driver.get(url)

time.sleep(1)


while(True):
    pass