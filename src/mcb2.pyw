'''
マルチクリップボードの拡張
この章のマルチクリップボード・プログラムを拡張して、棚からキーワードを削除するdelete <keyword>
コマンドライン引数を持つようにする。
次に、すべてのキーワードを削除するdeleteコマンドライン引数を追加する。
'''
#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: python.exe mcb2.pyw save <keyword> - クリップボードをキーワードに紐づけて保存
#        python.exe mcb2.pyw <keyword> - キーワードに紐づけられたテキストをクリップボードにコピー
#        python.exe mcb2.pyw list - 全キーワードをクリップボードにコピー
#        python.exe mcb2.pyw delete <keyword> - キーワードに紐づけたクリップボードを削除
#        python.exe mcb2.pyw delete - 全キーワードに紐づけたクリップボードを削除

import shelve, pyperclip, sys
from pathlib import Path

(Path.cwd() / 'MCB').mkdir(exist_ok=True)
mcbShelf = shelve.open('MCB/mcb')

if len(sys.argv) == 3:
    # Save clipboard content.
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    # Delete <keyword>.
    elif sys.argv[1].lower() == 'delete':
        if sys.argv[2] in mcbShelf:
            del mcbShelf[sys.argv[2]]

elif len(sys.argv) == 2:
    # Delete all content.
    if sys.argv[1].lower() == 'delete':
        mcbShelf.clear()
    # List keywords and load content.
    elif sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])


mcbShelf.close()
