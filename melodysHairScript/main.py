from pyautogui import *
from pynput.mouse import Listener, Button
import pyautogui
import time 
import keyboard
import win32api, win32con


positionsX = [];
positionsY = [];
r = [];
g = [];
b = [];
i = 0;


# Function called on a mouse click
def on_click(x, y, button, pressed):
    # Check if the left button was pressed
    if pressed and button == Button.left:
        # Print the click coordinates
        print(f'x={x} and y={y}')
        positionsX.append(x);
        positionsY.append(y);
    if not pressed:
        return False



print("calibrating, press on each of the blocks so that the program knows where to execute the click\n")

for i in range(0, 7):
    print(i+1, ": ")
    with Listener(on_click=on_click) as listener:
        listener.join()




def click(x, y):
    win32api.SetCursorPos((x,y))
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    win32api.SetCursorPos((100,100))



while keyboard.is_pressed('u') == False:
    pass

i = 0

for i in range(0,7):
    red, green, blue = pyautogui.pixel(positionsX[0], positionsY[0])
    r.append(red);
    g.append(green);
    b.append(blue);

while keyboard.is_pressed('y') == False:
    
    r, g, b = pyautogui.pixel(positionsX[0], positionsY[0])
    if r != r[0]:
        click(positionsX[0], positionsY[0])

    r, g, b = pyautogui.pixel(positionsX[1], positionsY[1])
    if r != r[1]:
        click(positionsX[1], positionsY[1])

    r, g, b = pyautogui.pixel(positionsX[2], positionsY[2])
    if r != r[2]:
        click(positionsX[2], positionsY[2])

    r, g, b = pyautogui.pixel(positionsX[3], positionsY[3])
    if r != r[3]:
        click(positionsX[3], positionsY[3])

    r, g, b = pyautogui.pixel(positionsX[4], positionsY[4])
    if r != r[4]:
        click(positionsX[4], positionsY[4])

    r, g, b = pyautogui.pixel(positionsX[5], positionsY[5])
    if r != r[5]:
        click(positionsX[5], positionsY[5])

    r, g, b = pyautogui.pixel(positionsX[6], positionsY[6])
    if r != r[6]:
        click(positionsX[6], positionsY[6])
        
    