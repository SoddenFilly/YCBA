from pynput.mouse import Button, Controller as Controller_mouse
from pynput.keyboard import Key, Controller as Controller_keyboard

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as Bsoup

import random
import time
import os

def FillText(text, typeSpeed, submitDelay):

    if isinstance(text, list):

        for string in text:

            if string != text[0]:
                keyboard.press(Key.tab)
                keyboard.release(Key.tab)

            string = list(string)
            for i in range(0, len(string)):
                keyboard.press(string[i])
                keyboard.release(string[i])
                time.sleep(typeSpeed)

    else:
        string = list(text)
        for i in range(0, len(string)):
            keyboard.press(string[i])
            keyboard.release(string[i])
            time.sleep(typeSpeed)
    
    time.sleep(0.1+submitDelay)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
# FillText("", 0.001, 0.2)

def DriverInst(webdriverDir):
    driver = webdriver.Chrome(webdriverDir)
    # driver = webdriver.Chrome(r"\chromedriver.exe")
    driver.maximize_window() # For maximizing window
    driver.implicitly_wait(20)
    return driver

def CompileVideoLinks(channel, driver):

    
    driver.get(f"https://www.youtube.com/c/{channel}/videos")

    time.sleep(1)
    
    if driver.title == "404 Not Found":
        driver.get(f"https://www.youtube.com/user/{channel}/videos")
        time.sleep(1)
        if driver.title == "404 Not Found":
            return

    localLinks = []
    while True:

        keyboard.press(Key.end)
        keyboard.release(Key.end)
        time.sleep(1)
        # print("eh")
        # container = driver.find_element_by_id("items")
        elements = driver.find_elements_by_id("thumbnail")
        if len(elements)-1 == len(localLinks):
            print("\nEND\n")
            break

        localLinks = []
        for e in elements:
            link = e.get_attribute('href')
            if link != None:
                localLinks.append(link)
        print(len(localLinks))

    time.sleep(2)

    return localLinks

def ListProcessing(subj, skips):
    # print(subj)
    subj_temp = []
    # skips = 2
    for i in range(0, len(subj), skips):
        subj_temp.append(subj[i])
        # print(subj_temp)
    # print(subj_temp)
    # print(len(subj_temp))
    return subj_temp

def STATIC():

    keyboard = Controller_keyboard()
    
    workingDir = os.getcwd()
    print(workingDir)
    webdriverDir = f"{workingDir}\\tools\\chromedriver.exe"
    print(webdriverDir)
    driver = DriverInst(webdriverDir)

    defaultChannels = ["EddievanderMeer", "monoman", "PaulDavids", "AKSTARENG", "SteveTerreberry", "PirateCrabUK", "CharlesBerthoud"]

    globalLinks = []
    for channel in defaultChannels:
        try:
            globalLinks.extend(CompileVideoLinks(channel, driver))
        except Exception as err: 
            print(f"\n\n{err}\n\n")

    driver.quit()

    return globalLinks

if __name__ == "__main__":

    links = STATIC()