import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver= webdriver.Chrome(executable_path='C:\\Users\\raval\\Documents\\chromedriver_win32\\chromedriver.exe')
driver.get('https://www.amazon.ca/')
driver.implicitly_wait(8)
driver.maximize_window()
electronics=driver.find_element_by_id("nav-hamburger-menu")
electronics.click()