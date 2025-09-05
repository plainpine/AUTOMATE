import pyautogui, time

# 5秒待っている間、メモ帳を開く
time.sleep(5)
pyautogui.keyDown('shift'); pyautogui.press('4'); pyautogui.keyUp('shift')
