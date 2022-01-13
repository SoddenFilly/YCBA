from pynput.mouse import Button, Controller as Controller_mouse
from pynput.keyboard import Key, Controller as Controller_keyboard

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as Bsoup

import random
import time
import os

def DriverInst(webdriverDir):
    
    driver = webdriver.Chrome(webdriverDir)
    driver.maximize_window() # For maximizing window
    driver.implicitly_wait(20)
    return driver

def STATIC():

    keyboard = Controller_keyboard()
    
    workingDir = os.getcwd()
    print(workingDir)
    webdriverDir = f"{workingDir}\\tools\\chromedriver.exe"
    print(webdriverDir)
    driver = DriverInst(webdriverDir)

    driver.get(f"https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    time.sleep(1)
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    time.sleep(16)
    driver.quit()

if __name__ == "__main__":

    STATIC()