from pynput.mouse import Button, Controller as Controller_mouse

import random
import time

mouse = Controller_mouse()

def mouseClick(posX, posY, isRight):
    mouse.position = (posX, posY) # Set pointer position
    if isRight == True:
        mouse.press(Button.right)
        mouse.release(Button.right)
    else:
        mouse.press(Button.left)
        mouse.release(Button.left)

time.sleep(5)

delay = 0.2
for f in range(30):
    
    mouseClick(75, 340, True)

    time.sleep(delay)

    mouseClick(100, 400, False)

    time.sleep(delay)

    mouseClick(850, 450, False)

    time.sleep(delay)