# 英語からピッグ・ラテンに変換
print('Enter the English message to translate into Pig Latin:')
message = input()
VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')
pigLatin = [] # ピッグラテンの単語のリスト

for word in message.split():
    # wordの先頭の英字でないものを分離する
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue

    # wordの末尾の英字でないものを分離する
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:-1]

    # wordがすべて大文字か、先頭のみ大文字かを覚えておく
    wasUpper = word.isupper()
    wasTitle = word.istitle()
    word = word.lower() # 交換のために、すべて小文字にする

    # wordの先頭の子音を分離する
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]

    # wordにピッグ・ラテンの語尾をつける
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'

    # 必用ならwordをすべて大文字か、先頭のみ大文字に戻す
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    # wordの先頭と末尾にあった英字でない文字を元に戻す
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)

# 単語のリストを１つの文字列に連結して表示する
print(' '.join(pigLatin))
