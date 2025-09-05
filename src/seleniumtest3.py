from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

browser = Firefox()
browser.get('https://login.metafilter.com')

user_elem = browser.find_element(By.ID,'user_name')
user_elem.send_keys('tempuser12345')
password_elem = browser.find_element(By.ID,'user_pass')
password_elem.send_keys('tn!FDBH85*3D3jb')
password_elem.submit()
