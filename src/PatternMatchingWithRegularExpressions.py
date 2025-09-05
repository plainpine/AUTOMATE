'''
PatternMatchingWithRegularExpressions

strip()メソッドの正規表現バージョン

文字列を受け取り、strip() 文字列メソッドと同じことを行う関数を書きます。
stripする文字列以外に引数が渡されない場合は、文字列の先頭と末尾から空白文字が取り除かれます。
そうでない場合は、関数の第2引数で指定された文字が文字列から取り除かれます。
'''

import re

def regexStrip(stripme, removeChars=None):
    if removeChars == None:
        return re.sub(r'(^ *)|( *$)', '', stripme)
    else:
        escapedRemoveChars = ''
        regexEscapes = ['*', '\\', '{', '}', '[', ']', '(', ')', '^', '$', '.', '+', '?', '|']
        for char in removeChars:
            if(char in regexEscapes):
                escapedRemoveChars += '\\' + char
        return re.sub('^' + escapedRemoveChars + '*|' + escapedRemoveChars + '*$', '', stripme)

# テスト用文字列（空白のみ取り除く）
testStrings = [ 'No spaces', ' leading space', '    lots of leading spaces', 'trailing space ',
                ' leading and trailing space ']
# テスト用文字列（*と空白を取り除く）
testStringsOptChars = ['  *** leading *** space', '****** leading and trailing space *****']

for testS in testStrings:
    print(testS)
    print(regexStrip(testS) == testS.strip())

for testOptS in testStringsOptChars:
    print(testOptS)
    print(regexStrip(testOptS, '*') == testOptS.strip('*'))

