#Implicit wait-Glboal wait
#Explicit wait-wait at specific location

from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver= webdriver.Chrome(executable_path='C:\\Users\\raval\\Documents\\chromedriver_win32\\chromedriver.exe')
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.find_element_by_css_selector("[class='search-keyword']").send_keys('ber')
#To check how many products gets diplayed if we write 'ber'
#go=driver.find_element_by_xpath("//div[@class='products']/div[1]/div[3]/button")
wait=WebDriverWait(driver,10)
#wait.until(expected_conditions.staleness_of(go))
wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH,"//div[@class='product']/div[3]/button")))
grocery=driver.find_elements_by_xpath("//div[@class='product']/div[3]/button")
#assert grocery==3
for item in grocery:

    item.click()
driver.find_element_by_css_selector("[alt='Cart']").click()

driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
#wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"[placeholder='Enter promo code']")))
driver.find_element_by_css_selector("[class='promoCode']").send_keys('rahulshettyacademy')
driver.find_element_by_css_selector("[class='promoBtn']").click()
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"[class='promoInfo']")))
print(driver.find_element_by_css_selector("[class='promoInfo']").text)

