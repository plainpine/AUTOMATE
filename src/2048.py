# seleniumのインポート
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# Firefoxの起動と「2048」への移動
browser = Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')  #「2048」のページのURL

# 「上右下左」をn回送信する関数
def send_allows(n):
    for i in range(n):
        html_elem.send_keys(Keys.UP) # 「上」を送信
        html_elem.send_keys(Keys.RIGHT) # 「右」を送信
        html_elem.send_keys(Keys.DOWN) # 「下」を送信
        html_elem.send_keys(Keys.LEFT) # 「左」を送信

# 「上右下左」を100回送信
html_elem = browser.find_element(By.TAG_NAME,'html')
send_allows(100)
