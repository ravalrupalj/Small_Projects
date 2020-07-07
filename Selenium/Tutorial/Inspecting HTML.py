from selenium import webdriver

driver= webdriver.Chrome(executable_path='C:\\Users\\raval\\Documents\\WebDrivers\\chromedriver_win32\\chromedriver.exe')
driver.get('https://rahulshettyacademy.com/angularpractice/')
driver.find_element_by_name('name').send_keys('Rupal')
driver.find_element_by_id('exampleCheck1').click()
