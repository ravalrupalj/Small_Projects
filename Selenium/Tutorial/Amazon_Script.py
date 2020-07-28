from selenium import webdriver

driver= webdriver.Chrome(executable_path='C:\\Users\\raval\\Documents\\chromedriver_win32\\chromedriver.exe')
driver.get('https://www.amazon.ca/')
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element_by_id("twotabsearchtextbox").send_keys("ashlin wallet")
driver.find_element_by_css_selector("input[value='Go']").click()
driver.find_element_by_xpath("//img[@alt='ASHLIN RFID Blocking Wallet| Made with #1 Grade Napa Genuine Leather Excellent Credit Card Protector |10 Credit Card Pockets']").click()
driver.find_element_by_id("add-to-cart-button").click()
driver.back()
driver.back()
driver.find_element_by_xpath("(//img[@alt=\"Ashlin RFID Blocking Men's SLIM BI-fold Wallet - 100% Genuine Leather wallet with lined currency compartment\"])[1]").click()
driver.find_element_by_id("add-to-cart-button").click()
driver.back()
driver.back()
driver.find_element_by_xpath("(//img[@alt='ASHLIN RFID Blocking Wallet| Made with #1 Grade Napa Genuine Leather Excellent Credit Card Protector |10 Credit Card Pockets'])[2]").click()
driver.find_element_by_id("add-to-cart-button").click()
driver.back()
driver.back()
driver.find_element_by_xpath("(//img[@alt=\"ASHLIN Men's Bi-fold Wallet - 100% Lambskin Napa | Double Billfold Section | Midnight Black [5748-07-01]\"])[1]").click()
driver.find_element_by_id("add-to-cart-button").click()

driver.find_element_by_xpath("//a[@id='hlb-view-cart-announce']").click()
assert "ASHLIN Men's Bi-fold Wallet - 100% Lambskin Napa | Double Billfold Section | Midnight Black [5748-07-01]"==driver.find_element_by_xpath("(//span[@class='a-size-medium sc-product-title a-text-bold'])[1]").text
print(driver.find_element_by_xpath("(//span[@class='a-size-medium sc-product-title a-text-bold'])[1]").text)
assert "ASHLIN RFID Blocking Wallet| Made with #1 Grade Napa Genuine Leather Excellent Credit Card Protector |10 Credit Card Pockets" ==driver.find_element_by_xpath("(//span[@class='a-size-medium sc-product-title a-text-bold'])[2]").text
print(driver.find_element_by_xpath("(//span[@class='a-size-medium sc-product-title a-text-bold'])[2]").text)
assert "Ashlin RFID Blocking Men's SLIM BI-fold Wallet - 100% Genuine Leather wallet with lined currency compartment" == driver.find_element_by_xpath("(//span[@class='a-size-medium sc-product-title a-text-bold'])[3]").text
print(driver.find_element_by_xpath("(//span[@class='a-size-medium sc-product-title a-text-bold'])[3]").text)
#assert "CDN$ 70.89" == driver.find_element_by_xpath("//span[@class='a-size-medium a-color-base sc-price sc-white-space-nowrap']").text
print(driver.find_element_by_xpath("//span[@class='a-size-medium a-color-base sc-price sc-white-space-nowrap']").text)
#driver.find_element_by_id("hlb-ptc-btn").click()
#driver.find_element_by_id("ap_email").send_keys("ravalrupalj@gmail.com")
#driver.find_element_by_id("continue").click()