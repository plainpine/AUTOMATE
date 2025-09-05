#! python3
# command line emailer.py - email a string of text
"""
コマンドラインで電子メールアドレスと文字列を受け取り、Seleniumを使って電子メールアカウントにログインし、
提供されたアドレスに文字列の電子メールを送信するプログラムを書いてください。 (このプログラムのために、
別の電子メールアカウントを設定するとよいでしょう)。

注：電子メールの扱いは複雑です。
多くの異なるユーザーが異なる設定をし、異なるタイプの電子メール・アカウントを使用しています。
この解決策はあなたには使えないかもしれないので、あなたの特定の設定に適したものを見つけなければなりません。
全体として、Eメールを送信するためのもっと良い方法があるので、このコードであまり時間を無駄にしないでください。
おそらく使うことはないでしょうから、seleniumがどのように動作するかを理解できれば、成功したと考えてください。
"""
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# メールの受信者、件名、本文、ログイン情報のユーザー入力
email_username = input('ユーザ名を入力してください\n')
email_password = input('パスワードを入力してください\n')
email_recipient = input('宛先を入力してください\n')
email_subject = input('件名を入力してください\n')
email_body = input('メールの文面を入力してください\n')

browser = Chrome()
browser.maximize_window()
browser.implicitly_wait(30)
browser.get('http://mail.google.com')
login_elem = browser.find_element(By.ID,'identifierId')
login_elem.send_keys(email_username)
next_elem = browser.find_element(By.ID,'identifierNext')
next_elem.click()
time.sleep(3)

password_elem = browser.find_element_by_name("password")
password_elem.send_keys(email_password)
pw_next_elem = browser.find_element(By.ID,'passwordNext')
pw_next_elem.click()
time.sleep(3)

html_elem = browser.find_element(By.TAG_NAME,'html')
html_elem.send_keys('c')
html_elem.send_keys(Keys.TAB)
html_elem.send_keys(email_recipient)
html_elem.send_keys(Keys.TAB)
html_elem.send_keys(email_subject)
html_elem.send_keys(Keys.TAB)
html_elem.send_keys(email_body)
html_elem.send_keys(Keys.ENTER)

print('Email was sent.')
