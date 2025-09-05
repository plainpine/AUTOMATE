#! python 3.5
# RegexSearch.py - フォルダ内のすべての txt ファイルを開き、
# ユーザが指定した正規表現にマッチする行を検索する。

import os, re
def search(regex, txt):
    searchRegex = re.compile(regex, re.I)
    result = searchRegex.findall(txt)
    print(result)

while True:
    dirs = input('検索したいフォルダの絶対パスを入力してください\n')
    if os.path.exists(dirs) == True:
        print('このフォルダは存在します')
        break
user_search = input('正規表現を入力してください\n')


folder = os.listdir(dirs)

for file in folder:
    if file.endswith('.txt'):
        print(os.path.join(dirs, file))
        txtfile = open(os.path.join(dirs, file), 'r+')
        msg = txtfile.read()
        search(user_search, msg)
