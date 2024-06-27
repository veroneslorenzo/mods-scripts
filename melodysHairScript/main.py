from pyautogui import *
from pynput.mouse import Listener, Button
import pyautogui
import time 
import keyboard
import win32api, win32con


# Function called on a mouse click
def on_click(x, y, button, pressed):
    # Check if the left button was pressed
    if pressed and button == Button.left:
        # Print the click coordinates
        print(f'x={x} and y={y}')


# Initialize the Listener to monitor mouse clicks
with Listener(on_click=on_click) as listener:
    listener.join()

"""
def click(x, y):
    win32api.SetCursorPos((x,y))
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    win32api.SetCursorPos((100,100))



while keyboard.is_pressed('u') == False:
    pass

while keyboard.is_pressed('y') == False:
    
    r, g, b = pyautogui.pixel(743, 424)
    if r == 141 and g == 69 and b == 94:
        click(741, 480)

    r, g, b = pyautogui.pixel(816, 424)
    if r == 106 and g == 80 and b == 12:
        click(814, 477)

    r, g, b = pyautogui.pixel(888, 424)
    if r == 44 and g == 76 and b == 10:
        click(886, 478)

    r, g, b = pyautogui.pixel(960, 424)
    if r == 33 and g == 43 and b == 14:
        click(958, 480)

    r, g, b = pyautogui.pixel(1032, 424)
    if r == 47 and g == 15 and b == 70:
        click(1030, 479)

    r, g, b = pyautogui.pixel(1103, 424)
    if r == 29 and g == 31 and b == 92:
        click(1101, 480)

    r, g, b = pyautogui.pixel(1176, 424)
    if r == 19 and g == 67 and b == 90:
        click(1174, 479)
        
    
"""