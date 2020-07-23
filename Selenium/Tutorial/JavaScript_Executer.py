import time

from selenium import webdriver

driver= webdriver.Chrome(executable_path='C:\\Users\\raval\\Documents\\chromedriver_win32\\chromedriver.exe')
driver.get('https://rahulshettyacademy.com/angularpractice/')
#driver.find_element_by_name('name').send_keys('Rupal')
#print(driver.find_element_by_name("name").text)
#print(driver.find_element_by_name("name").get_attribute("value"))
#print(driver.execute_script("return document.getElementsByName('name')[0].value"))
#driver.find_element_by_css_selector("a[href*='shop']") -->different way
#driver.find_element_by_css_selector("ul[class='navbar-nav'] li:nth-child(2)").click()
#using JavaScript
shopbutton=driver.find_element_by_css_selector("ul[class='navbar-nav'] li:nth-child(2)")
driver.execute_script("arguments[0].click();",shopbutton)
#to scroll down
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")