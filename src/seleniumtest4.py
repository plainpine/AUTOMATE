from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

browser = Firefox()
browser.get('https://nostarch.com')

Html_elem = browser.find_element(By.TAG_NAME,'html')
Html_elem.send_keys(Keys.END)    # 末尾にスクロール
time.sleep(3)
Html_elem.send_keys(Keys.HOME)   # 先頭にスクロール
