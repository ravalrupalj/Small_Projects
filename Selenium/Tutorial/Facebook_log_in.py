from selenium import webdriver

driver= webdriver.Chrome(executable_path='C:\\Users\\raval\\Documents\\WebDrivers\\chromedriver_win32\\chromedriver.exe')
driver.get('https://www.facebook.com/')
driver.find_element_by_css_selector('input[name="email"]').send_keys('ID')
driver.find_element_by_css_selector('input[name="pass"]').send_keys('PASSWORD')
driver.find_element_by_css_selector('input[value="Log In"]').click()
#driver.find_element_by_css_selector('div[class*="sj5x9vvc"]').click()
