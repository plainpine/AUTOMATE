from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

browser = Firefox()
browser.get('https://inventwithpython.com')

link_elem = browser.find_element(By.LINK_TEXT, 'available for preorders on the No Starch Press website')
type(link_elem)
print(type(link_elem))

link_elem.click() # "available for preorders on the No Starch Press website" のリンクをたどる
