from selenium import webdriver
import time
driver= webdriver.Chrome(executable_path='C:\\Users\\raval\\Documents\\WebDrivers\\chromedriver_win32\\chromedriver.exe')
driver.get('https://login.salesforce.com/?locale=ca')
driver.find_element_by_css_selector('#username').send_keys('Rupal')
driver.find_element_by_css_selector('input.password').send_keys('Crazy')
time.sleep(3)
driver.find_element_by_css_selector('.password').clear()