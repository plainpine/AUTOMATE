from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome
import time

def scrape_dynamic_page(url):
    # Chromeオプションの設定
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # ヘッドレスモードで実行（画面表示なし）
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # WebDriverの初期化
    driver = Chrome()

    try:
        # URLに移動
        driver.get(url)

        # JavaScriptが実行されるまで待機（例：特定の要素が表示されるまで）
        wait = WebDriverWait(driver, 10)
        # この例では、id="content"の要素が表示されるまで待機
        content = wait.until(EC.presence_of_element_located((By.ID, "content")))

        # ページのHTMLを取得
        html = driver.page_source

        #print(html)

        return(html)

    finally:
        # ブラウザを閉じる
        driver.quit()


def main():
    import requests, sys, webbrowser, bs4
    url = 'https://pypi.org/search/?q=' + ' '.join(sys.argv[1:])  # スクレイピング対象のURL
    #url = 'https://pypi.org/search/?q=' + ' ' + 'term'  # スクレイピング対象のURL
    data = scrape_dynamic_page(url)

    # 上位の検索結果のリンクを取得する
    soup = bs4.BeautifulSoup(data, 'html.parser')
    #print(soup)

    link_elems = soup.select('.package-snippet')
    #print(link_elems)

    # 各結果をブラウザのタブで開く
    num_open = min(5, len(link_elems))

    #print(num_open)

    for i in range(num_open):
        url_to_open = 'https://pypi.org' + link_elems[i].get('href')
        print('Opening', url_to_open)
        webbrowser.open(url_to_open)

if __name__ == "__main__":
    main()
