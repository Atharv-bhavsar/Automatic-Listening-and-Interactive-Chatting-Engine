# File with screenshot and camera functions

# Import necessary modules
import os  # Module for interacting with the operating system
import ai_speak  # Module for AI voice output
import time  # Module for time-related functions
import pyautogui  # Module for GUI automation


# Function to take a screenshot
def screenshot():
    # print("Starting capture, switch to desired window")
    # ai_speak.speak("Starting capture, switch to desired window")
    if not os.path.exists("Captures"):
        os.mkdir("Captures")
    # for i in range(5, 0, -1):
    #     print(i)
    #     ai_speak.speak(i)
    image = pyautogui.screenshot()
    image.save("Captures/screenshot.jpg")
    # print("Screenshot captured")
    # ai_speak.speak("Screenshot captured")
    os.startfile("Captures")
    return "Screenshot captured"


# Function to take a photo using the camera
def camera():
    # print("Starting application")
    # ai_speak.speak("Starting application")
    pyautogui.press("super")
    time.sleep(2)
    pyautogui.typewrite("camera")
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(2)
    # print("Smile")
    # ai_speak.speak("Smile")
    time.sleep(10)
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.hotkey("alt", "f4")
    time.sleep(2)
    # print("Photo saved")
    # ai_speak.speak("Photo saved")
    os.startfile("C:\\Users\\MEHUL\\OneDrive\\Pictures\\Camera Roll")
    return "Image Captured"
