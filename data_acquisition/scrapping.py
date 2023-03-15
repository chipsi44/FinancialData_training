from selenium import webdriver
from selenium.webdriver.common.by import By


def get_the_page_firefox(link) :
        '''options = webdriver.FirefoxOptions()
        options.accept_insecure_certs = True
        driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=options
        )'''
        driver = webdriver.Firefox()
        driver.set_page_load_timeout(60)
        driver.get(link)
        return driver

def Accept_the_cookies_financeYahoo(driver) :

    scroll_button = driver.find_element(By.ID, "scroll-down-btn")
    scroll_button.click()

    cookie_button = driver.find_element(By.XPATH, "//button[@class='btn secondary accept-all ' and @name='agree']")
    cookie_button.click()

#start scrapping
def get_header_financeYahoo(driver) :
    thead_element = driver.find_element(By.TAG_NAME,"thead")
    th_elem = thead_element.find_elements(By.TAG_NAME,"th")
    my_header_list = []
    for elem in th_elem[:-1] : 
        my_header_list.append(elem.text)
    return my_header_list

def get_entreprise(driver) :
    tbody_element = driver.find_element(By.TAG_NAME,"tbody")
    tr_elem_from_tbody  = tbody_element.find_elements(By.TAG_NAME,"tr")
    entreprise_list = []
    for selenium_elem_tr in tr_elem_from_tbody :
        td_elem_in_tr = selenium_elem_tr.find_elements(By.TAG_NAME,"td")
        entreprise_list.append([])
        for selenium_elem_td in td_elem_in_tr :
            entreprise_list[-1].append(selenium_elem_td.text)
    return entreprise_list


def main_scrap_financeYahoo(link) :
    driver = get_the_page_firefox(link)
    Accept_the_cookies_financeYahoo(driver)
    my_header_list = get_header_financeYahoo(driver)
    entreprise_list = get_entreprise(driver)
    try :
        driver.close()
        driver.quit()
    except : 
        print("Driver not closed")
    return entreprise_list,my_header_list
