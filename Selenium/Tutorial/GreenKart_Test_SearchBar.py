import time

from selenium import webdriver

driver= webdriver.Chrome(executable_path='C:\\Users\\raval\\Documents\\chromedriver_win32\\chromedriver.exe')
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
expected=['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
driver.find_element_by_css_selector("[class='search-keyword']").send_keys('ber')
time.sleep(3)
grocery=driver.find_elements_by_xpath("//div[@class='product-action']/button")
l=[]
for item in grocery:
    l.append(item.find_element_by_xpath("parent::div/parent::div/h4").text)
    item.click()
assert expected==l