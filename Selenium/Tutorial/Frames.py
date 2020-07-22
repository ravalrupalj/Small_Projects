from selenium import webdriver

driver= webdriver.Chrome(executable_path='C:\\Users\\raval\\Documents\\chromedriver_win32\\chromedriver.exe')
#https://the-internet.herokuapp.com/
driver.get('https://the-internet.herokuapp.com/iframe')
#Check parent's tag name. it should start like iframe or framset or frame
driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("I can do Automate")
driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text)