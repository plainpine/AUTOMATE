import pyautogui, time

# 5秒待っている間、メモ帳を開く
time.sleep(5)
pyautogui.click(100+1920, 200); pyautogui.write('Hello, world!')
