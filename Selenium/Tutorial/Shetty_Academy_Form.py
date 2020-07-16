from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
driver= webdriver.Chrome(executable_path='C:\\Users\\raval\\Documents\\chromedriver_win32\\chromedriver.exe')
#driver= webdriver.Firefox(executable_path='C:\\Users\\raval\\Documents\\geckodriver-v0.26.0-win64\\geckodriver.exe')
driver.get('https://rahulshettyacademy.com/angularpractice/')
#driver.find_element_by_name('name').send_keys('Rupal')
driver.find_element_by_id('exampleCheck1').click()
driver.find_element_by_css_selector('input[class="ng-untouched ng-pristine ng-valid"]').send_keys('Rupal')
driver.find_element_by_name('email').send_keys('ravalrupalj@gmail.com')
driver.find_element_by_xpath('//input[@class="btn btn-success"]').click()
#print(driver.find_element_by_class_name('alert-success').text)
message=driver.find_element_by_class_name('alert-success').text
assert 'success' in message
# Select class provide the methods to handle the options in dropdown
dropdown=Select(driver.find_element_by_id('exampleFormControlSelect1'))
dropdown.select_by_visible_text('Female')
time.sleep(3)
dropdown.select_by_index(0)