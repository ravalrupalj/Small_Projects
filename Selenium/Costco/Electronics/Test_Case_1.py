import time

from selenium import webdriver
#Test Case 1
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver= webdriver.Chrome(executable_path='C:\\Users\\raval\\Documents\\chromedriver_win32\\chromedriver.exe')
driver.get('https://www.costco.ca/')
driver.maximize_window()


driver.find_element_by_xpath("//input[@value='ON']").click()
driver.find_element_by_id("language-region-set").click()

