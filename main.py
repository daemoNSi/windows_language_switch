from win32con import WM_INPUTLANGCHANGEREQUEST
from win32gui import GetForegroundWindow
from win32api import SendMessage
import keyboard
import pyautogui
import time


while True:
    try:
        if keyboard.is_pressed('ctrl+1'):
            if SendMessage(GetForegroundWindow(), WM_INPUTLANGCHANGEREQUEST, 0, 0x4090409) == 0:
                pass
            time.sleep(1)
        elif keyboard.is_pressed('ctrl+2'):
            if SendMessage(GetForegroundWindow(), WM_INPUTLANGCHANGEREQUEST, 0, 0x4110411) == 0:
                with pyautogui.hold('shift'):
                    pyautogui.press('capslock')
            time.sleep(1)
        elif keyboard.is_pressed('ctrl+3'):
            if SendMessage(GetForegroundWindow(), WM_INPUTLANGCHANGEREQUEST, 0, 0x4190419) == 0:
                pass
            time.sleep(1)
    except:
        pass
