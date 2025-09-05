import pyautogui
import time

def nudge_mouse():
    while True:
        # Get current mouse position
        x, y = pyautogui.position()

        # Move the mouse slightly
        pyautogui.moveTo(x + 1, y + 1, duration=0.1)
        pyautogui.moveTo(x, y, duration=0.1)

        # Wait 10 seconds before the next nudge
        time.sleep(10)

if __name__ == "__main__":
    print("Mouse nudge script started. Press Ctrl+C to stop.")
    try:
        nudge_mouse()
    except KeyboardInterrupt:
        print("Script stopped.")
