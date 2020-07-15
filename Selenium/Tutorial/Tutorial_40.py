import time
from selenium import webdriver

driver= webdriver.Chrome(executable_path='C:\\Users\\raval\\Documents\\chromedriver_win32\\chromedriver.exe')
driver.get('https://login.salesforce.com/?locale=ca')
driver.find_element_by_css_selector('#username').send_keys('Rupal')
driver.find_element_by_css_selector('input.password').send_keys('Crazy')
time.sleep(3)
driver.find_element_by_css_selector('.password').clear()
driver.find_element_by_link_text('Forgot Your Password?').click()
time.sleep(3)
driver.find_element_by_xpath('//a[text()="Cancel"]').click()
print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)