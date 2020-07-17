from selenium import webdriver
import time

from selenium.webdriver.support import select

driver= webdriver.Chrome(executable_path='C:\\Users\\raval\\Documents\\chromedriver_win32\\chromedriver.exe')
driver.get('https://www.makemytrip.com/')
time.sleep(1)
element=driver.find_element_by_css_selector('[id="fromCity"]')
element.send_keys('del')
time.sleep(2)
cities=driver.find_elements_by_css_selector("p[class*='blackText']")
#print(len(cities))
for city in cities:
    city.text
    if city.text=='Del Rio, United States':
        driver.execute_script("arguments[4].click();", city)
        print(city.text)
        city.click()
        break