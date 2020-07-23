import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver= webdriver.Chrome(executable_path='C:\\Users\\raval\\Documents\\chromedriver_win32\\chromedriver.exe')
driver.get('https://rahulshettyacademy.com/angularpractice/')
driver.implicitly_wait(10)
driver.find_element_by_css_selector("ul[class='navbar-nav'] li:nth-child(2)").click()
driver.find_element_by_xpath("//a[text()='Blackberry']/parent::h4/parent::div/parent::div/div[2]/button").click()
checkout=driver.find_element_by_css_selector("a[class*='btn-primary']")
checkout.click()
driver.find_element_by_css_selector("button[class*='btn-success']").click()
driver.find_element_by_id("country").send_keys("Ind")
#Explicit wait (instead of implicit wait)
#wait=WebDriverWait(driver,10)
#wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
#driver.find_element_by_link_text("India").click()
country=driver.find_elements_by_xpath("//div[@class='suggestions']/ul/li/a")
for each in country:
    if each.text =="India":
        each.click()
        break
driver.find_element_by_css_selector("label[for='checkbox2']").click()
driver.find_element_by_css_selector("[value='Purchase']").click()
success=driver.find_element_by_css_selector("div[class*='alert']").text
assert "Success! Thank you!" in  success
print(driver.find_element_by_css_selector("div[class*='alert']").text)

driver.get_screenshot_as_file("screen.png")