#! python3
# scheduledComicDownloader.py

import bs4, os, requests

# フォルダ作成
folderName = 'web-comics'
os.makedirs(folderName, exist_ok=True)

# フォルダにない場合コミックをダウンロード
def check_for_update(comicUrl):

	# ファイル名を取得
	fileName = os.path.basename(comicUrl)
	
	# すでにフォルダに存在しているか確認
	if fileName in os.listdir(folderName):
		print('本日の更新はありません. 最新のコミックは %s.' % comicUrl)
	
	# ない場合はダウンロード
	else:
		print('ダウンロード中 %s...' % comicUrl)

		res = requests.get(comicUrl)
		res.raise_for_status()
		imageFile = open(os.path.join(folderName, fileName), 'wb')
		for chunk in res.iter_content(100000):
			imageFile.write(chunk)
		imageFile.close()

def get_qwantz_comic():

	# コミックのurl
	site = 'http://www.qwantz.com'
	
	# 画像取得用urlをテキストから抽出
	res = requests.get(site)
	res.raise_for_status()
	soup = bs4.BeautifulSoup(res.text, 'html.parser')
	
	# 画像のurlを取得
	comicElem = soup.select('.comic')
	comicUrlShort = comicElem[0].get('src')
	comicUrl = site + '/' + comicUrlShort
	
	# 画像があるか確認
	if comicElem == 0:
		print('コミックがありません %s.' % site)

	# ダウンロード開始
	else:
		check_for_update(comicUrl)
	
def get_xkcd_comic():

	# コミックのurl取得	
	site = 'https://xkcd.com'
	
	# 画像取得用urlをテキストから抽出
	res = requests.get(site)
	res.raise_for_status()
	soup = bs4.BeautifulSoup(res.text, 'html.parser')
	
	# 画像のurlを取得
	comicElem = soup.select('#comic > img')
	comicUrlShort = comicElem[0].get('src')
	comicUrl = 'http:' + comicUrlShort
	
	# 画像があるか確認
	if comicElem == 0:
		print('コミックがありません %s.' % site)

	# ダウンロード開始
	else:
		check_for_update(comicUrl)

get_qwantz_comic()
get_xkcd_comic()
