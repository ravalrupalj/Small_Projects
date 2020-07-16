from selenium import webdriver
import time

from selenium.webdriver.support.wait import WebDriverWait

driver= webdriver.Chrome(executable_path='C:\\Users\\raval\\Documents\\chromedriver_win32\\chromedriver.exe')
driver.get('https://www.makemytrip.com/')
time.sleep(2)

element = driver.find_element_by_css_selector('[id="fromCity"]')
#webdriver.ActionChains(driver).move_to_element(element).click(element ).perform()

#driver.find_element_by_id("fromCity").click()


element.send_keys('del')
time.sleep(2)
countries=driver.find_elements_by_css_selector("p[class*='blackText']")
for city in countries:
   city.text
   if city.text=='Del Rio, United States':
       webdriver.ActionChains(driver).move_to_element(city).click(city).perform()

       break