import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver= webdriver.Chrome(executable_path='C:\\Users\\raval\\Documents\\chromedriver_win32\\chromedriver.exe')
driver.get('https://www.amazon.ca/')
driver.implicitly_wait(8)
driver.maximize_window()
#Test case 1
electronics=driver.find_element_by_id("nav-hamburger-menu")
electronics.click()
driver.find_element_by_xpath("//div[contains(text(),'Music, Movies & TV Shows')]").click()
#Test case 2
driver.find_element_by_xpath("//a[contains(text(),'All Movies & TV Shows')]").click()
assert driver.find_element_by_xpath("//h1[contains(text(),'Movies & TV Series')]").text == "Movies & TV Series"
#Test case 3
driver.find_element_by_xpath("//a[contains(text(),'Comedy')]").click()
assert driver.find_element_by_xpath("//b[contains(text(),'Comedy')]").text =="Comedy"
#Test case 4
driver.find_element_by_xpath("//span[@class='a-size-small a-color-base'][contains(text(),'Movies')]").click()
assert driver.find_element_by_xpath("//span[@class='a-color-state a-text-bold']").text=="Movies"
Movies_List=driver.find_elements_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")
for each in Movies_List:
    print(each.text)
driver.back()
#Test case 5
driver.find_element_by_xpath("//span[@class='a-size-small a-color-base'][contains(text(),'TV')]").click()
assert driver.find_element_by_xpath("//span[@class='a-color-state a-text-bold']").text=="TV"
TV_List=driver.find_elements_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")
for each in TV_List:
    print(each.text)
driver.back()
#Test case 6
driver.find_element_by_xpath("//span[contains(text(),'Drama')]").click()
assert driver.find_element_by_xpath("//span[@class='a-color-state a-text-bold']").text=="Drama"

driver.back()
#Test case 7
assert driver.find_element_by_xpath("//span[@class='a-color-state a-text-bold'][contains(text(),'Exercise & Fitness')]").text=="Exercise & Fitness"