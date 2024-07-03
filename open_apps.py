# File to open and close apps using ALICE

# Import necessary modules
import ai_speak
import pyautogui
import time


def start(query):
    # Modify the query to handle "open" commands and special characters
    query = query.replace("open", "")
    query = query.replace(" plus plus ", "++")

    print("Opening application...")
    ai_speak.speak("Opening application...")
    time.sleep(2)

    # Simulate pressing Windows key
    pyautogui.press("super")
    time.sleep(2)

    # Type the application name
    pyautogui.typewrite(query)
    time.sleep(2)

    # Press Enter to open the application
    pyautogui.press("enter")
