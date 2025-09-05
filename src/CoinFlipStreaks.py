import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # 100個の裏表のリストを作るコード
    hundred_flips = []
    for flip in range(100):
        if random.randint(0, 1) == 0:
            hundred_flips.append('H')
        else:
            hundred_flips.append('T')
    # ６連続の裏または表を見つけるコード
    all_flips = ''
    for i in range(len(hundred_flips) - 1):
        all_flips += hundred_flips[i]

    if 'HHHHHH' in all_flips or 'TTTTTT' in all_flips:
        numberOfStreaks += 1

print(f'同じ面が６連続出現する確率: %s%%' % (numberOfStreaks / 100))
