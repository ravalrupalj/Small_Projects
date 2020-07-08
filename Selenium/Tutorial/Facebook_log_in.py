#This script will go and write happy birthday on people's wall that has birthday today!

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver= webdriver.Chrome(executable_path='C:\\Users\\raval\\Documents\\WebDrivers\\chromedriver_win32\\chromedriver.exe')
driver.get('https://www.facebook.com/')
driver.find_element_by_css_selector('input[name="email"]').send_keys('ID')
driver.find_element_by_css_selector('input[name="pass"]').send_keys('Password')
driver.find_element_by_css_selector('input[value="Log In"]').click()
time.sleep(3)
driver.get('https://www.facebook.com/events/birthdays/')
time.sleep(3)
for i in driver.find_elements_by_css_selector("div[class='_1mf _1mj']"):
    i.send_keys('Happy Birthday!!')
    i.send_keys(Keys.RETURN)

