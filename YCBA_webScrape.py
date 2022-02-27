from pynput.mouse import Button, Controller as Controller_mouse
from pynput.keyboard import Key, Controller as Controller_keyboard

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as Bsoup

import random
import time
import os

def FillText(text, typeSpeed, startDelay, submitDelay, keyboard=Controller_keyboard):

    time.sleep(0.1+startDelay)

    if "\n" in text:
        text = text.split("\n")[1:-1]
        # print()
        multiLine = True
    else:
        multiLine = False

    if isinstance(text, list) and multiLine == True:
        
        for line in text:
            for string in line:

                # if string != text[0]:
                #     keyboard.press(Key.tab)
                #     keyboard.release(Key.tab)

                string = list(string)
                for i in range(0, len(string)):
                    keyboard.press(string[i])
                    keyboard.release(string[i])
                    time.sleep(typeSpeed)

            keyboard.press(Key.enter)
            keyboard.release(Key.enter)

    elif isinstance(text, list):

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

    if multiLine == False:
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

def DriverInst(webdriverDir, headless):
    if headless == True:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920x1080")

        driver = webdriver.Chrome(executable_path=webdriverDir, chrome_options=chrome_options)
    
    else:
        driver = webdriver.Chrome(executable_path=webdriverDir)
        driver.maximize_window() # For maximizing window
        driver.implicitly_wait(20)

    return driver

def CompileVideoLinks(channel, driver, keyboard):

    try:
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
            try:
                elements = driver.find_elements_by_id("thumbnail")
                if len(elements)-1 == len(localLinks):
                    print("\nEND\n")
                    break

                localLinks = []
                for e in elements:
                    link = e.get_attribute('href')
                    if link != None:
                        localLinks.append(link)
                # print(len(localLinks))
            except Exception as e:
                print("exection-b:", e)
                quit("QUIT")
                return -1

        time.sleep(2)

        return localLinks
    
    except Exception as e:
        print("exeption-a:", e)
        quit("QUIT")
        return -1

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

def STATIC(getVids=False, validateChannel=False, channelList=["monoman"], secret=False):

    keyboard = Controller_keyboard()
    
    # fileLocationPath = os.path.dirname(os.path.realpath(__file__))
    fileLocationPath = os.getcwd()

    webdriverDir = f"{fileLocationPath}\\tools\\chromedriver.exe"

    if getVids == True:
        driver = DriverInst(webdriverDir, False)

        # defaultChannels = ["EddievanderMeer", "monoman"]#, "PaulDavids", "AKSTARENG", "SteveTerreberry", "PirateCrabUK", "CharlesBerthoud"]

        globalLinks = []
        for channel in channelList:
            try:
                globalLinks.extend(CompileVideoLinks(channel, driver, keyboard))
            except Exception as err: 
                print(f"\nERROR-MESSAGE:\n{err}\n\n")

            if -1 in globalLinks:
                return -1
                
        driver.quit()

        return globalLinks

    elif validateChannel == True:
        driver = DriverInst(webdriverDir, True)

        driver.get(f"https://www.youtube.com/c/{channelList[0]}/videos")

        time.sleep(1)
        
        if driver.title == "404 Not Found":
            driver.get(f"https://www.youtube.com/user/{channelList[0]}/videos")
            time.sleep(1)
            if driver.title == "404 Not Found":
                return False
        
        return True
    
    elif secret == True:
        driver = DriverInst(webdriverDir, False)

        driver.get(f"https://youtu.be/dQw4w9WgXcQ")

if __name__ == "__main__":

    links = STATIC(False, True)