import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver= webdriver.Chrome(executable_path='C:\\Users\\raval\\Documents\\chromedriver_win32\\chromedriver.exe')
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.find_element_by_css_selector("[class='search-keyword']").send_keys('ber')
time.sleep(3)
#name=driver.find_elements_by_css_selector("h4.product-name")
grocery=driver.find_elements_by_xpath("//div[@class='product-action']/button")
#child to grand parent
#//div[@class='product-action']/button/parent::div/parent::div/h4

l=[]
for item in grocery:
    l.append(item.find_element_by_xpath("parent::div/parent::div/h4").text)
    item.click()
print(l)
driver.find_element_by_css_selector("[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(3)
product_name=driver.find_elements_by_css_selector("p.product-name")
final_product=[]
for final in product_name:
    final_product.append(final.text)
assert l==final_product
price_before_dic=driver.find_element_by_css_selector("span.discountAmt").text
driver.find_element_by_css_selector("[placeholder='Enter promo code']").send_keys('rahulshettyacademy')
driver.find_element_by_css_selector("[class='promoBtn']").click()
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoInfo")))
price_after_Disc=driver.find_element_by_css_selector("span.discountAmt").text
assert int(price_before_dic)>float(price_after_Disc)
print(driver.find_element_by_css_selector("[class='promoInfo']").text)
total=driver.find_elements_by_xpath("//tr/td[5]/p")
sum=0
for each in total:
    sum=sum+int(each.text)
print(sum)

total2=int(driver.find_element_by_css_selector("span.totAmt").text)
assert sum==total2
