import pyautogui
fw = pyautogui.getActiveWindow()
fw.width # 現在のウィンドウの幅

fw.topleft # 現在のウィンドウの位置
(174, 153)
fw.width = 1000 # 幅を変更
fw.topleft = (800+1920, 400) # ウィンドウうを移動
