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
#get header
thead_element = driver.find_element(By.TAG_NAME,"thead")
th_elem = thead_element.find_elements(By.TAG_NAME,"th")
my_header_list = []
for elem in th_elem[1:-1] : 
    my_header_list.append(elem.text)
print(my_header_list)
#get entreprise
tbody_element = driver.find_element(By.TAG_NAME,"tbody")
all_body_list = tbody_element.text.split('\n')
#get rid of entreprise tag name
entreprise_info_list = [elem for elem in all_body_list if len(elem) >= 5]
#loop over the entreprise and create entreprise list
work_list = entreprise_info_list[0]

new_list = work_list.split(' ')
