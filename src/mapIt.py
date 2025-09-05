#! python3
# mapIt.py - コマンドラインやクリップボードに指定した住所の地図を開く

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # debug
    print('arg = ' + str(sys.argv[1:]))
    # コマンドラインから住所を取得する
    address = ' '.join(sys.argv[1:])
    # debug
    print('address = ' + address)  
else:
    # debug
    print('pyperclip = ' + pyperclip.paste())
    # クリップボードから住所を取得する
    address = pyperclip.paste()
    # debug
    print('address = ' + address)  

webbrowser.open('https://www.google.com/maps/place/' + address)
