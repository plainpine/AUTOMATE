# Conwayのライフゲーム
import random, time, copy
WIDTH = 60
HEIGHT = 20
# セルを格納するリストのs区政
nextCells = []
for x in range(WIDTH):
    column = [] # 新しい列を作成
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#') # 生きたセルを追加
        else:
            column.append(' ') # 死んだセルを追加
    nextCells.append(column) # nextCells は列のリストのリスト
while True: # メインプログラムループ
    print('\n\n\n\n\n') # ステップ澗を改行で分ける
    currentCells = copy.deepcopy(nextCells)
    # currentCellsを表示
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='') # # か スペースを表示
        print() # 行末で改行
    # 現在のセルに基づき次のステップのセルを表示
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # 隣接座標を取得
            # `% WIDTH` により leftCoord を 0 and WIDTH - 1 の値にする
            leftCoord  = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT
            # 生きた隣接セルのカウント
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1 # 左上が生きたセル
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1 # 上が生きたセル
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1 # 右上が生きたセル
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1 # 左が生きたセル
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1 # 右が生きたセル
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1 # 左下が生きたセル
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1 # 下が生きたセル
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1 # 右下が生きたセル
            # Conwayのライフゲームのルールに基づきセルを設定
            if currentCells[x][y] == '#' and (numNeighbors == 2 or
numNeighbors == 3):
                # 生きたセルに隣接する生きたセルが2個か３個
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                # 死んだセルに隣接する生きたセルが３個
                nextCells[x][y] = '#'
            else:
                # その他の場合は死んだセルになる
                nextCells[x][y] = ' '
    time.sleep(1) # ちらつきを防ぐため１秒待つ
