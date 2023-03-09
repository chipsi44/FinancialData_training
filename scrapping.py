from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://finance.yahoo.com/most-active?offset=0&count=100")

#Accept the cookies

scroll_button = driver.find_element(By.ID, "scroll-down-btn")
scroll_button.click()

cookie_button = driver.find_element(By.XPATH, "//button[@class='btn secondary accept-all ' and @name='agree']")
cookie_button.click()

#start scrapping