#! python3
# searchpypi.py - pypiの検索結果をいくつか開く

import requests, sys, webbrowser, bs4

print('Searching...')  # 検索結果をダウンロード中のテキストを表示
res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
#print('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

#print(res.raise_for_status())
#print(res.text)

# 上位の検索結果のリンクを取得する
soup = bs4.BeautifulSoup(res.text, 'html.parser')
print(soup)

link_elems = soup.select('package-snippet')
#print(link_elems)


# 各結果をブラウザのタブで開く
num_open = min(5, len(link_elems))

#print(num_open)

for i in range(num_open):
    url_to_open = 'https://pypi.org' + link_elems[i].get('href')
    print('Opening', url_to_open)
    webbrowser.open(url_to_open)

