import time

from selenium import webdriver

driver= webdriver.Chrome(executable_path='C:\\Users\\raval\\Documents\\chromedriver_win32\\chromedriver.exe')
driver.get('https://the-internet.herokuapp.com/windows')
driver.find_element_by_link_text("Click Here").click()
childwindow=driver.window_handles[1]
#("parentid","childid")
driver.switch_to.window(childwindow)
print(driver.find_element_by_tag_name("h3").text)
driver.close()
driver.switch_to.window(driver.window_handles[0])
print(driver.find_element_by_tag_name("h3").text)
assert "Opening a new window" ==driver.find_element_by_tag_name("h3").text
driver.close()
