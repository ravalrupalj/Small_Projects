import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver= webdriver.Chrome(executable_path='C:\\Users\\raval\\Documents\\chromedriver_win32\\chromedriver.exe')
driver.get('https://www.amazon.ca/')
driver.implicitly_wait(8)
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
LCD_LED_TVs=driver.find_elements_by_xpath("//div[@class='a-section a-spacing-none']/h2")
for each in LCD_LED_TVs:
   assert 'LCD' or 'LED' in each.text

driver.find_element_by_xpath("//span[@class='a-size-base a-color-base a-text-bold'][contains(text(),'LCD & LED')]").click()
driver.find_element_by_xpath("//span[@class='a-size-base a-color-base'][contains(text(),'OLED')]").click()
OLED_TVs=driver.find_elements_by_xpath("//div[@class='a-section a-spacing-none']/h2")
for each in OLED_TVs:
  assert "OLED" in each.text


driver.find_element_by_xpath("//span[@class='a-size-base a-color-base a-text-bold'][contains(text(),'OLED')]").click()
driver.find_element_by_xpath("//li[@aria-label='4K Ultra HD']/span/a/div").click()
ultra_HD=driver.find_elements_by_xpath("//div[@class='a-section a-spacing-none']/h2")
for each in ultra_HD:
   assert "4K" and "Smart" in each.text

driver.find_element_by_xpath("//li[@aria-label='4K Ultra HD']/span/a/div").click()
driver.find_element_by_xpath("//span[contains(text(),'720p HD Ready')]").click()
HD720_Ready=driver.find_elements_by_xpath("//div[@class='a-section a-spacing-none']/h2")
for each in HD720_Ready:
   assert "720" in each.text

driver.find_element_by_xpath("//span[@class='a-size-base a-color-base a-text-bold'][contains(text(),'720p HD Ready')]").click()
driver.find_element_by_xpath("//span[@class='a-size-base a-color-base a-text-bold'][contains(text(),'Smart')]").click()
driver.find_element_by_xpath("//span[@class='a-size-small a-color-base s-ref-text-link s-ref-link-cursor'][contains(text(),'1080p Full HD')]").click()
#for each in Full1080_Full_HD:
#   assert "1080" in Full1080_Full_HD
driver.find_element_by_xpath("//span[@class='a-size-base a-color-base a-text-bold'][contains(text(),'1080p Full HD')]").click()
driver.find_element_by_xpath("//div[@data-a-input-name='s-ref-checkbox-Hisense']/label/span/span").click()
Hisense_Tvs=driver.find_elements_by_xpath("//div[@class='a-section a-spacing-none']/h2")
for each in Hisense_Tvs:
   assert "Hisense" or "HISENSE" in each.text
driver.find_element_by_xpath("//span[@class='a-size-base a-color-base a-text-bold'][contains(text(),'Hisense')]").click()
driver.find_element_by_xpath("//span[contains(text(),'PROSCAN')]").click()
Proscan_Tvs=driver.find_elements_by_xpath("//div[@class='a-section a-spacing-none']/h2")
for each in Proscan_Tvs:
   assert "Proscan" or "PROSCAN" in Proscan_Tvs

driver.find_element_by_xpath("//span[@class='a-size-base a-color-base a-text-bold'][contains(text(),'PROSCAN')]").click()
#driver.find_element_by_xpath("//span[@class='a-size-small a-color-base s-ref-text-link s-ref-link-cursor'][contains(text(),'Sony')]").click()
#Sony_Tvs=driver.find_elements_by_xpath("//div[@class='a-section a-spacing-none']/h2")
#for each in Sony_Tvs:
#   assert "Sony" in each.text
#driver.find_element_by_xpath("//span[@class='a-size-base a-color-base a-text-bold'][contains(text(),'Sony')]").click()
driver.find_element_by_xpath("//span[@class='a-size-small a-color-base s-ref-text-link s-ref-link-cursor'][contains(text(),'SANSUI')]").click()
Sansui_Tvs=driver.find_elements_by_xpath("//div[@class='a-section a-spacing-none']/h2")
for each in Sansui_Tvs:
   assert "Sansui" or "SANSUI" in each.text
driver.find_element_by_xpath("//span[@class='a-size-base a-color-base a-text-bold'][contains(text(),'SANSUI')]").click()
driver.find_element_by_xpath("//span[contains(text(),'Smart / Internet')]").click()
driver.find_element_by_xpath("//span[@class='a-size-base a-color-base'][contains(text(),'Samsung')]").click()
driver.find_element_by_xpath("//span[@class='a-size-base a-color-base'][contains(text(),'TCL')]").click()
TCL_Samsung=driver.find_elements_by_xpath("//div[@class='a-section a-spacing-none']/h2")
for each in TCL_Samsung:
   assert "TCL" or "Samsung" in TCL_Samsung

driver.find_element_by_xpath("//span[@class='a-size-base a-color-base'][contains(text(),'LG')]").click()
TCL_Samsung_LG=driver.find_elements_by_xpath("//div[@class='a-section a-spacing-none']/h2")

for each in TCL_Samsung_LG:
   assert "TCL" or "Samsung" or "LG" in each.text
driver.find_element_by_xpath("//li[@aria-label='4K Ultra HD']/span/a/div").click()
TCL_Samsung_LG_Ultra_HD=driver.find_elements_by_xpath("//div[@class='a-section a-spacing-none']/h2")
for each in TCL_Samsung_LG_Ultra_HD:
   assert "TCL" or "Samsung" or "LG" and "Ultra HD" in each.text

driver.find_element_by_xpath("//div[@id='brandsRefinements']/ul/li/span/a/span[2]").click()
ALL_TV_Ultra=driver.find_elements_by_xpath("//div[@class='a-section a-spacing-none']/h2")
for each in ALL_TV_Ultra:
   assert "TV" and "4K" in each.text

driver.find_element_by_xpath("//ul[@aria-labelledby='p_n_feature_twelve_browse-bin-title']/li/span/a/span[2]").click()
driver.find_element_by_xpath("//input[@id='low-price']").send_keys("200")
driver.find_element_by_xpath("//input[@id='high-price']").send_keys("500")
driver.find_element_by_xpath("//span[@class='a-button a-spacing-top-mini a-button-base s-small-margin-left']").click()
select=Select(driver.find_element_by_id("a-autoid-11"))
select.select_by_visible_text('Price: Low to High')

