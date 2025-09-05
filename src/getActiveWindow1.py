import pyautogui

fw = pyautogui.getActiveWindow()
fw
print(fw)

str(fw)
print(str(fw))

fw.title
print(fw.title)

fw.size
print(fw.size)

fw.left, fw.top, fw.right, fw.bottom
print(fw.left, fw.top, fw.right, fw.bottom)

fw.topleft
print(fw.topleft)

fw.area
print(fw.area)

pyautogui.click(fw.left + 10, fw.top + 20)
