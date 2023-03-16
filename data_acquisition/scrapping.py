from selenium import webdriver
from selenium.webdriver.common.by import By

def get_the_page_firefox(link) :
        '''
        Function that interact with selenium grid throught the port 4444 and Firefox.

        Args : 
            link : str, link to the firefox webpage. In this project it's a YahooFinance page
        Return : 
            driver : selenium object, connected to the firefox link
        '''
        #Connect to selenium grid
        options = webdriver.FirefoxOptions()
        options.accept_insecure_certs = True
        driver = webdriver.Remote(
        command_executor='http://selenium-container:4444/wd/hub',
        options=options
        )
        #Help to get less crash to connection timeout
        driver.set_page_load_timeout(60)
        #Connect to the link
        driver.get(link)
        return driver

def Accept_the_cookies_financeYahoo(driver) :
    '''
    This function is made to accept the cookies on the web page finance Yahoo

    Args : 
         driver -> selenium object, already connected to the firefox YahooFinance page
    '''
    scroll_button = driver.find_element(By.ID, "scroll-down-btn")
    scroll_button.click()

    cookie_button = driver.find_element(By.XPATH, "//button[@class='btn secondary accept-all ' and @name='agree']")
    cookie_button.click()

#start scrapping
def get_header_financeYahoo(driver) :
    '''
    Scrapes the header for a CSV file from Yahoo Finance and returns it as a list.

    Args:
        driver -> selenium object, already connected to the firefox YahooFinance page
    return :     
        my_header_list -> List of strings.
    '''
    thead_element = driver.find_element(By.TAG_NAME,"thead")
    th_elem = thead_element.find_elements(By.TAG_NAME,"th")
    my_header_list = []
    for elem in th_elem[:-1] : 
        my_header_list.append(elem.text)
    return my_header_list

def get_entreprise(driver) :
    '''
    This function is used to get all the info about the differents entreprise stock availabe on the web page.

    args : 
        driver -> selenium object, already connected to the firefox YahooFinance page
    return : 
        entreprise_list -> list of str, contains info about the stock of differents entreprise.
    '''
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
    '''
    This function incorporates all of the above functions to navigate to a Firefox web page and scrape data.

    Args : 
        link -> Str, link of the firefox webpage
    return : 
        entreprise_list -> list of str, contains info about the stock of differents entreprise.
        my_header_list -> List of str.
    '''
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

