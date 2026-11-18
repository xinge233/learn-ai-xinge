from selenium import webdriver
driver=webdriver.Edge()
driver.get("https://www.baidu.com")
print(driver.title)