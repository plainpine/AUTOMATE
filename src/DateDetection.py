import re

def is_valid_date(date_str):
    # 正規表現パターン：DD/MM/YYYY
    dateRegex = re.compile(r'''(
        (3[01]|[12][0-9]|0?[1-9])       # 日 1-31 or 01-31
        [/]                             # 区切
        ([1][0-2]|0?[1-9])              # 月 1-12 or 01-12
        [/]                             # 区切
        ([12]\d{3})                     # 年 1000-2999
        )''', re.VERBOSE)               # https://www.debuggex.com/

    # 正規表現で日付のフォーマットをチェック
    if not re.match(dateRegex, date_str):
        return False

    # 日、月、年の部分を取得
    day, month, year = map(int, date_str.split('/'))

    # 月が31日以内かチェック
    if month in [1, 3, 5, 7, 8, 10, 12] and day > 31:
        return False

    # 月が30日以内かチェック
    if month in [4, 6, 9, 11] and day > 30:
        return False

    # うるう年の2月かチェック
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            # うるう年の場合
            if day > 29:
                return False
        else:
            # うるう年でない場合
            if day > 28:
                return False

    # すべてのチェックを通過した場合は、妥当な日付とみなす
    return True


# テスト
while True:
    date_str=input('Enter Date in DD/MM/YYYY: ')
    if date_str == "":
        break
    if is_valid_date(date_str):
        print(f'{date_str}は有効な日付です。')
    else:
        print(f'{date_str}は無効な日付です。')
