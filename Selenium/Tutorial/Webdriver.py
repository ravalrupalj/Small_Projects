from selenium import webdriver

driver= webdriver.Chrome(executable_path='C:\\Users\\raval\\Documents\\WebDrivers\\chromedriver_win32\\chromedriver.exe')
driver.get('file:///C:/Users/raval/Documents/Website/First_Website.html')
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.refresh()
driver.minimize_window()
driver.get('https://www.facebook.com/')
driver.back()

driver.close()