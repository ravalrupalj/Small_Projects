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
driver.find_element_by_xpath("//a[contains(text(),'Cell Phones & Accessories')]").click()
driver.find_element_by_xpath("//a[contains(text(),'Apple')]").click()
Apple_Phones=driver.find_elements_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")
for phone in Apple_Phones:
   assert "Apple" in phone.text

driver.find_element_by_xpath("//span[contains(text(),'Samsung')]").click()
driver.find_element_by_xpath("//span[@class='a-size-base a-color-base a-text-bold'][contains(text(),'Apple')]").click()
Samsung_Phones=driver.find_elements_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")
for phone in Samsung_Phones:
   assert "Samsung" in phone.text

driver.find_element_by_xpath("//span[contains(text(),'Motorola')]").click()
driver.find_element_by_xpath("//span[@class='a-size-base a-color-base a-text-bold'][contains(text(),'Samsung')]").click()
Motorola_Phones=driver.find_elements_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")
for phone in Motorola_Phones:
   assert "Motorola" or "Moto" in phone.text

driver.find_element_by_xpath("//span[contains(text(),'HUAWEI')]").click()
driver.find_element_by_xpath("//span[@class='a-size-base a-color-base a-text-bold'][contains(text(),'Motorola')]").click()
Huawei_Phones=driver.find_elements_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")
for phone in Huawei_Phones:
   assert "Honor" or "Huawei" or "Huawei" in phone.text

driver.find_element_by_xpath("//span[contains(text(),'UMIDIGI')]").click()
driver.find_element_by_xpath("//span[@class='a-size-base a-color-base a-text-bold'][contains(text(),'HUAWEI')]").click()
UMIDIGI_Phones=driver.find_elements_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")
for phone in UMIDIGI_Phones:
   assert "UMIDIGI" in phone.text


driver.find_element_by_xpath("//span[contains(text(),'Easyfone')]").click()
driver.find_element_by_xpath("//span[@class='a-size-base a-color-base a-text-bold'][contains(text(),'UMIDIGI')]").click()
Easyfone_Phones=driver.find_elements_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")
for phone in Easyfone_Phones:
   assert "Easyfone" in phone.text


driver.find_element_by_xpath("//span[@class='a-size-base a-color-base a-text-bold'][contains(text(),'Easyfone')]").click()
driver.find_element_by_xpath("//input[@id='low-price']").send_keys("200")
driver.find_element_by_xpath("//input[@id='high-price']").send_keys("1000")
driver.find_element_by_xpath("//span[@id='a-autoid-3']/span").click()

driver.find_element_by_xpath("//span[contains(text(),' Cell Phones & Accessories')]").click()
driver.find_element_by_xpath("//a[contains(text(),'Tablets')]").click()
driver.find_element_by_xpath("//input[@name='s-ref-checkbox-Samsung']").click()
Samsung_Tablets=driver.find_elements_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")
for tablets in Samsung_Tablets:
   assert "Samsung" or "Galaxy" in tablets.text

driver.find_element_by_xpath("//span[contains(text(),'Apple')]").click()
driver.find_element_by_xpath("//span[@class='a-size-base a-color-base a-text-bold'][contains(text(),'Samsung')]").click()
Apple_Tablets=driver.find_elements_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")
for tablets in Apple_Tablets:
   assert "Apple" in tablets.text

driver.find_element_by_xpath("//span[contains(text(),'vankyo')]").click()
driver.find_element_by_xpath("//span[@class='a-size-base a-color-base a-text-bold'][contains(text(),'Apple')]").click()
Vankyo_tablets=driver.find_elements_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")
for tablets in Vankyo_tablets:
   assert "Vankyo" or "VANKYO" in tablets.text

driver.find_element_by_xpath("//span[contains(text(),'Clear')]").click()
tablets=driver.find_elements_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")
for tablet in tablets:
   assert "Tablet" in tablet.text

driver.find_element_by_xpath("//a[contains(text(),'Apple')]").click()
list=driver.find_elements_by_xpath("//div[@class='sg-col-inner']/div/h2/a")
for i in list:
   print(i.text)
   i.click()
   break
print(driver.find_element_by_xpath("//span[@id='priceblock_ourprice']").text)
driver.find_element_by_xpath("//input[@id='add-to-cart-button']").click()
driver.find_element_by_xpath("//span[@id='nav-cart-count']").click()
assert "New Apple iPad (10.2-Inch, Wi-Fi, 32GB) - Space Gray (Latest Model)"== driver.find_element_by_xpath("//span[@class='a-size-medium sc-product-title a-text-bold']").text
assert "CDN$ 488.98"==driver.find_element_by_xpath("//span[@class='a-size-medium a-color-base sc-price sc-white-space-nowrap sc-product-price a-text-bold']").text
