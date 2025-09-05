import pyautogui
for i in range(10): # マウスを正方形に動かす
    pyautogui.moveTo(100+1920, 100, duration=0.25)
    pyautogui.moveTo(200+1920, 100, duration=0.25)
    pyautogui.moveTo(200+1920, 200, duration=0.25)
    pyautogui.moveTo(100+1920, 200, duration=0.25)
