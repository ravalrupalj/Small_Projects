from selenium import webdriver
chromeoption=webdriver.ChromeOptions()
chromeoption.add_argument('--start-maximized')
chromeoption.add_argument("headless")
chromeoption.add_argument("--ignore-certificate-errors")
driver= webdriver.Chrome(executable_path='C:\\Users\\raval\\Documents\\chromedriver_win32\\chromedriver.exe',options=chromeoption)
driver.get('https://rahulshettyacademy.com/angularpractice/')
print(driver.title)