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

while(True):
    pass