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
time.sleep(3)
#To check how many products gets diplayed if we write 'ber'
grocery=driver.find_elements_by_xpath("//div[@class='products']/div")
#assert grocery==3
for item in grocery:
    add=item.find_element_by_css_selector("div[class='product-action'] button")
    add.click()
driver.find_element_by_css_selector("[alt='Cart']").click()

driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoCode")))

driver.find_element_by_css_selector("[placeholder='Enter promo code']").send_keys('rahulshettyacademy')
driver.find_element_by_css_selector("[class='promoBtn']").click()
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoInfo")))
print(driver.find_element_by_css_selector("[class='promoInfo']").text)

