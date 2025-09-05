import pyautogui
try:
    location = pyautogui.locateOnScreen('pc.png')
    print(location)
except:
    print('画像が見つかりませんでした。')

