from selenium import webdriver
import time
driver= webdriver.Chrome(executable_path='C:\\Users\\raval\\Documents\\chromedriver_win32\\chromedriver.exe')
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.find_element_by_id('name').send_keys('option3')
driver.find_element_by_id('alertbtn').click()
alert=driver.switch_to.alert
print(alert.text)
assert 'option3' in alert.text
alert.accept()
time.sleep(2)
driver.find_element_by_id('confirmbtn').click()
alert=driver.switch_to.alert
alert.dismiss()