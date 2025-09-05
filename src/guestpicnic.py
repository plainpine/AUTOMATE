allGuests = {'アリス': {'リンゴ': 5, 'プレッツェル': 12},
             'ボブ': {'ハムサンド': 3, 'リンゴ': 2},
             'キャロル': {'コップ': 3, 'アップルパイ': 1}}
def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought
print('持ち物の数:')
print(' - リンゴ ' + str(totalBrought(allGuests, 'リンゴ')))
print(' - コップ ' + str(totalBrought(allGuests, 'コップ')))
print(' - ケーキ ' + str(totalBrought(allGuests, 'ケーキ')))
print(' - ハムサンド ' + str(totalBrought(allGuests, 'ハムサンド')))
print(' - アップルパイ ' + str(totalBrought(allGuests, 'アップルパイ')))
