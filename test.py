from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("Test Execution Started")
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Remote(
command_executor='http://localhost:4444/wd/hub',
options=options
)
#maximize the window size
driver.maximize_window()
time.sleep(10)
#navigate to browserstack.com
driver.get("https://www.browserstack.com/")
#click on the Get started for free button
buton = driver.find_element(By.LINK_TEXT,"Get started free")
buton.click()
time.sleep(3)
#close the browser
driver.close()
driver.quit()
print("Test Execution Successfully Completed!")