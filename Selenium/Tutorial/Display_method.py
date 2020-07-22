from selenium import webdriver
from selenium.webdriver import ActionChains

driver= webdriver.Chrome(executable_path='C:\\Users\\raval\\Documents\\chromedriver_win32\\chromedriver.exe')
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
assert driver.find_element_by_id("displayed-text").is_displayed()
print(driver.find_element_by_id("displayed-text").is_displayed())
driver.find_element_by_id("hide-textbox").click()
assert not driver.find_element_by_id("displayed-text").is_displayed()
print(driver.find_element_by_id("displayed-text").is_displayed())