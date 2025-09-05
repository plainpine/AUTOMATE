#! python3
# StrongPasswordDetection.py
"""
正規表現を使って、渡されたパスワード文字列が強力であることを確認する関数を書きなさい
強力なパスワードとは、少なくとも8文字の長さで、大文字と小文字の両方を含み、少なくとも1桁の数字を持つものと定義します
文字列の強度を検証するために、複数の正規表現パターンに対して文字列をテストする必要があるかもしれません
"""

import re

# 文字列の強度を検証するためregex_countを使用し、関数開始時に0に設定します
# これは、パスワードが期待値を満たす判定に使用されます
# forループはそれぞれの正規表現をループし、基準のひとつでも満たさなければループを抜けます
# それぞれの正規表現が成功すると、regex_countの値に1が加算されます
# ループが終了し、正規表現検索に4回成功すると、パスワードは十分に強力であるというメッセージが表示されます
def strong_password(password):
    regex_count = 0
    for regex in regex_list:
        if regex.search(password) is None:
            print('Sorry, your password is not strong enough')
            break
        else:
            regex_count += 1
            continue
    if regex_count == 4:
        print('Congrats. Your password is strong enough!')


# まず、問題で与えられたすべての期待に応える正規表現を作成します
# 以下の条件を満たす必要があります
# 1) 少なくとも8文字
# 2) 少なくとも1つの大文字
# 3) 少なくとも1つの小文字
# 4) 少なくとも1つの数字
# 正規表現は厄介です！
# すべての記号、括弧、エスケープ文字が正しい場所に配置されていることを確認してください
# これには練習が必要です！
# 慣れるまで、正規表現を1つずつテストしてみるといいでしょう

length_regex = re.compile('.{8,}')
lower_case_regex = re.compile('[a-z]+')
upper_case_regex = re.compile('[A-Z]+')
digit_regex = re.compile('[\d]+')

# 上記で作成した正規表現のリストを作成します
regex_list = [length_regex,
              lower_case_regex,
              upper_case_regex,
              digit_regex]

# パスワードを入力するためのユーザー入力
pw = input('Please type in a password:\n')
strong_password(pw)
