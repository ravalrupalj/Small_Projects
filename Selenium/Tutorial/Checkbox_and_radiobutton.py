from selenium import webdriver

driver= webdriver.Chrome(executable_path='C:\\Users\\raval\\Documents\\chromedriver_win32\\chromedriver.exe')
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
#driver.find_element_by_id('checkBoxOption2').click()
box=driver.find_elements_by_css_selector("[type='checkbox']")
for i in box:
    if i.get_attribute('value')== 'option2':
        i.click()
        assert i.is_selected()
driver.find_element_by_css_selector("[value='radio3']").click()
#OR
radiobuttons=driver.find_elements_by_name('radioButton')
radiobuttons[2].click()
assert radiobuttons[2].is_selected()