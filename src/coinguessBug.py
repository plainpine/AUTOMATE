# 演習プロジェクト 11.8.1
# 不具合

import random

guess =''

while guess not in ('表', '裏'):
    print('コインの表裏を当ててください。表か裏を入力してください：')
    guess = input()

toss = random.randint(0, 1) # 0は裏、1は表

if toss == guess:
    print('当たり！')
else:
    print('はずれ！もう一回当てて！')
    guess = input()
    if toss == guess:
        print('当たり！')
    else:
        print('はずれ。このゲームは苦手ですね。')

