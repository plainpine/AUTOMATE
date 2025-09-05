import pyautogui
for i in range(10):
    pyautogui.move(100, 0, duration=0.25)   # 右
    pyautogui.move(0, 100, duration=0.25)   # 下
    pyautogui.move(-100, 0, duration=0.25)  # 左
    pyautogui.move(0, -100, duration=0.25)  # 上
