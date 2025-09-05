#! python3
# mclip.py - A multi-clipboard program.
TEXT = {'agree': """そうですね。私も賛同します。それが良いと思います。""",
        'busy': """すみませんが、今週後半か来週にしていただけませんか？""",
        'upsell': """これを毎月の寄付にすることを検討していただけませんか？"""}
import sys, pyperclip
if len(sys.argv) < 2:
    print('使い方: py mclip.py [キーフレーズ名]')
    print('キーフレーズに対応するテキストをクリップボードにコピーします。')
    sys.exit()
keyphrase = sys.argv[1]    # first command line arg is the keyphrase
if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print(keyphrase + 'のテキストをクリップボードにコピーしました。')
else:
    print(keyphrase + 'に対応するテキストはありません')
