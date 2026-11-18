from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Edge()
driver.get("https://www.baidu.com")
search_box=driver.find_element(By.ID,"chat-textarea")
search_box.send_keys("success")
search_box.send_keys(Keys.RETURN)
time.sleep(3)
driver.quit()
