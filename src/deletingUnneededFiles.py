'''
不要なファイルの削除
不要だが巨大なファイルやフォルダが、ハードドライブの容量の大部分を占めていることはよくあることです。
コンピュータの空き容量を確保しようとするなら、不要なファイルの中でも特に巨大なものを削除するのが一番得策です。
しかし、まずはそれらを見つけなければなりません。
フォルダツリーを見て回り、ファイルサイズが100MBを超えるものなど、特別に大きなファイルやフォルダを探すプログラムを作りましょう。
（ファイルのサイズを得るには、osモジュールのos.path.getsize()が使えることを覚えておいてください。）
これらのファイルを絶対パスとともに画面に表示します。
'''

import os
from pathlib import Path

def pathInputAndCheck():
    while True:
        folderPath = Path(input('フォルダのパスを入力してください: '))
        try:
            if folderPath.is_dir:
                return folderPath
            else:
                print('不正なパスです')
        except OSError:
            print('不正なパスです')


def bigFilesSize():
    totalSize, biggestFile = 0, [0, 0, 0]
    for foldername, subfolders, filenames in os.walk(folderPath):
        for filename in filenames:
            fileSize = round((os.path.getsize(
                f'{foldername}\{filename}'))/(1024 * 1024))
            if fileSize > biggestFile[2]:
                biggestFile = []
                biggestFile = [foldername ,filename, fileSize]
            if fileSize > 100:
                totalSize += fileSize
                print(f'{foldername}\{filename} is {fileSize} MB')
                # send2trash.send2trash(f'{foldername}/{filename}')
    print(f'最大ファイルとサイズ: {biggestFile[0]}\{biggestFile[1]} {biggestFile[2]} MB ')
    print(f'大きなファイルのサイズ合計: {totalSize} MB ')

folderPath = pathInputAndCheck()
bigFilesSize()
