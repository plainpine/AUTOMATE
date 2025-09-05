import pyautogui

pyautogui.position() # 現在のマウス位置を取得する
print(pyautogui.position())

pyautogui.position() # 現在のマウス位置を再度取得する
print(pyautogui.position())

p = pyautogui.position() # 再度取得する
p
print(p)

p[0] # インデックス 0　はX座標
print(p[0])

p.x # ｘ属性でもＸ座標を取得可能
print(p.x)
