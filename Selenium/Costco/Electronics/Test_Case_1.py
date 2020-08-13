import time
from selenium import webdriver
driver= webdriver.Chrome(executable_path='C:\\Users\\raval\\Documents\\chromedriver_win32\\chromedriver.exe')
driver.get('https://www.amazon.ca/')
driver.implicitly_wait(5)
driver.maximize_window()
electronics=driver.find_element_by_id("nav-hamburger-menu")
electronics.click()
list_Category=driver.find_elements_by_xpath("//a[@class='hmenu-item']/div")
for each in list_Category:
   if each.text=='Electronics, Computers & Office':
      each.click()

Electro=driver.find_element_by_xpath("//div[contains(text(),'electronics')]").text
assert 'ELECTRONICS' == Electro

driver.find_element_by_link_text("TV & Home Theatre").click()
list_electronics=driver.find_element_by_xpath("//div[@class='fst-h1-st pageBanner']/p").text
assert 'Smart TVs , 4K Ultra HD TVs , LCD & LED TVs , OLED TVs , Blu-ray Players , Streaming Media Players , Sound Bars , Projectors , Audio & Video Accessories'==list_electronics

driver.find_element_by_link_text("Smart TVs").click()
l=driver.find_elements_by_xpath("//div[@class='a-section a-spacing-none']/h2/a/span")
for each in l:
   print(each.text)
   assert 'Smart' and "TV" in each.text

driver.find_element_by_xpath("//span[@class='a-size-base a-color-base'][contains(text(),'TCL')]").click()
TCL_TV=driver.find_element_by_xpath("//div[@class='a-section a-spacing-none']/h2/a/span").text
assert "TCL" in TCL_TV

driver.find_element_by_xpath("//span[@class='a-size-base a-color-base a-text-bold'][contains(text(),'TCL')]").click()
driver.find_element_by_xpath("//span[@class='a-size-base a-color-base'][contains(text(),'Samsung')]").click()
Samsung_TV=driver.find_elements_by_xpath("//div[@class='a-section a-spacing-none']/h2")
for each in Samsung_TV:
   assert "Samsung" in each.text

driver.find_element_by_xpath("//span[@class='a-size-base a-color-base a-text-bold'][contains(text(),'Samsung')]").click()
driver.find_element_by_xpath("//span[@class='a-size-base a-color-base'][contains(text(),'LG')]").click()

LG_TV=driver.find_elements_by_xpath("//div[@class='a-section a-spacing-none']/h2")
for each in LG_TV:
   assert "LG" in each.text

driver.find_element_by_xpath("//span[@class='a-size-base a-color-base a-text-bold'][contains(text(),'LG')]").click()
#driver.find_element_by_xpath("//span[contains(text(),'50 to 59')]").click()
#TVsize=driver.find_elements_by_xpath("//div[@class='a-section a-spacing-none']/h2")
#for each in TVsize:
#    assert each.text in range(50,59)
driver.find_element_by_xpath("//span[contains(text(),'LCD & LED')]").click()
LCD_LED=driver.find_elements_by_xpath("//div[@class='a-section a-spacing-none']/h2")
for each in LCD_LED:
   assert 'LCD' or 'LED' in each.text