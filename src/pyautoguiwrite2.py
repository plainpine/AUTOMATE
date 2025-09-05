import pyperclip, pyautogui, time

def mywrite(s):
    hkey = 'ctrl'
    saved_clipboad = pyperclip.paste()
    pyperclip.copy(s)
    pyautogui.hotkey(hkey, 'v')
    pyperclip.copy(saved_clipboad)

# 5秒待っている間、メモ帳を開く
time.sleep(5)
pyautogui.click(100+1920, 200); mywrite('初めまして！')
