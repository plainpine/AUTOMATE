import pyautogui, time

# 5秒待っている間、操作したいウィンドウをアクティブにしてください
time.sleep(5)

fw = pyautogui.getActiveWindow()
fw.isMaximized # ウィンドウが最大化されていればTrue
print(fw.isMaximized)
time.sleep(5)

fw.isMinimized # ウィンドウが最小化されていればTrue
print(fw.isMinimized)
time.sleep(5)

fw.isActive # ウィンドウがアクティブならTrue
print(fw.isActive)
time.sleep(5)

fw.maximize() # ウィンドウを最大化
fw.isMaximized
print(fw.isMaximized)
time.sleep(5)

fw.restore() # 最小化/最大化を取り消す
fw.minimize() # ウィンドウを最小化
time.sleep(5)

# 5秒待っている間、他のウィンドウをアクティブにしてください
time.sleep(5)
fw.activate() # ウィンドウがアクティブに戻る
fw.close() # ウィンドウを閉じる
