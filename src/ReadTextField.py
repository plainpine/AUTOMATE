import pyautogui
import pygetwindow as gw
import pyperclip
import time

def copy_text_from_notepad():
    # Find the Notepad window
    windows = gw.getWindowsWithTitle('Notepad')
    if not windows:
        print("No Notepad window found.")
        return

    notepad = windows[0]

    # Bring the Notepad window to the front
    notepad.activate()
    time.sleep(0.5)  # Wait for the window to come to the front

    # Click in the middle of the Notepad text area
    click_x = notepad.left + 100
    click_y = notepad.top + 200
    pyautogui.click(click_x, click_y)

    # Select all and copy
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.1)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.1)  # Wait for clipboard to update

    # Get clipboard content
    text = pyperclip.paste()
    print("Copied text:\n", text)

if __name__ == "__main__":
    copy_text_from_notepad()

