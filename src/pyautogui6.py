import pyautogui, time
time.sleep(5)
pyautogui.click()    # お絵描きアプリをクリックしてフォーカスする
distance = 300
change = 20
while distance > 0:
    pyautogui.drag(distance, 0, duration=0.2)   # 右に移動
    distance = distance - change
    pyautogui.drag(0, distance, duration=0.2)   # 下に移動
    pyautogui.drag(-distance, 0, duration=0.2)  # 左に移動
    distance = distance - change
    pyautogui.drag(0, -distance, duration=0.2)  # 上に移動
