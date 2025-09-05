#! python3
# phoneAndEmail.py - クリップボードから電話番号とメアドを検索する
import pyperclip, re

# 電話番号の正規表現を作る。
# 日本の場合
#    (\d{3}|\(\0\d{0,3}\))?            # 市外局番
#    (\s|-)?                           # 区切り
#    (\d{1,4})                         # 市内局番
#    (\s|-)?                           # 区切り
#    (\d{3,4})                         # 加入者番号
#    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # 内線番号
#    )''', re.VERBOSE)

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # 市外局番
    (\s|-|\.)?                        # 区切り
    (\d{3})                           # 市内局番
    (\s|-|\.)                         # 区切り
    (\d{4})                           # 加入者番号
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # 内線番号
    )''', re.VERBOSE)

# 電子メールの正規表現を作る。
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # ユーザー名
    @                      # @ 記号
    [a-zA-Z0-9.-]+         # ドメイン名
    (\.[a-zA-Z]{2,4})      # ドットなんとか
    )''', re.VERBOSE)

# クリップボードのテキストを検索する
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

# 検索結果をクリップボードに貼り付ける
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('クリップボードにコピーしました:')
    print('\n'.join(matches))
else:
    print('電話番号やメールアドレスは見つかりませんでした。')
