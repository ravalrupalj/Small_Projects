from selenium import webdriver
driver= webdriver.Chrome(executable_path='C:\\Users\\raval\\Documents\\chromedriver_win32\\chromedriver.exe')
driver.get('localhost:8080')
driver.implicitly_wait(8)
driver.find_element_by_css_selector("#login-form-username").send_keys("ravalrupalj")
driver.find_element_by_css_selector("#login-form-password").send_keys("awesomelife")
driver.find_element_by_css_selector("#login").click()
driver.find_element_by_xpath("//a[@title='View recent projects and browse a list of projects']").click()
driver.find_element_by_css_selector("#admin_main_proj_link_lnk").click()