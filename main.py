from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from secrets import username, password

firefox = webdriver.Firefox()
firefox.get('https://github.com/login')
firefox.maximize_window()
sleep(1)

firefox.find_element_by_id('login_field').send_keys(username)
firefox.find_element_by_id('password').send_keys(password)
firefox.find_element_by_id('password').send_keys(Keys.RETURN)
