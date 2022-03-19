from controller.webdriver import Element
from selenium import webdriver

driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
driver.get('https://www.google.com/')

search_area = Element(driver, 'search')
search_area.as_class = 'gLFyf'
search_area.find_by_class()
search_area.set_by_class('google')


search_botton = Element(driver, 'login')
search_botton.as_class = 'gb_1'
search_botton.find_by_class()
print(search_botton.click_by_class())

