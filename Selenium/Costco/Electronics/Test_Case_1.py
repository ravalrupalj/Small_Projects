import time

from selenium import webdriver


driver= webdriver.Chrome(executable_path='C:\\Users\\raval\\Documents\\chromedriver_win32\\chromedriver.exe')
driver.get('https://www.amazon.ca/')
driver.implicitly_wait(5)
driver.maximize_window()
electronics=driver.find_element_by_id("nav-hamburger-menu")
electronics.click()
driver.find_element_by_link_text("Electronics, Computers & Office").click()
driver.find_element_by_link_text("TV & Home Theatre").click()
driver.find_element_by_link_text("Smart TVs").click()
l=driver.find_elements_by_xpath("//div[@class='a-section a-spacing-none']/h2/a/span")
for each in l:
   print(each.text)
   assert 'Smart' in each.text
   assert 'TV' in each.text
driver.find_element_by_xpath("//div[@id='brandsRefinements']/ul/li[1]/span").click()