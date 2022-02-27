from pynput.mouse import Button, Controller as Controller_mouse
from pynput.keyboard import Key, Controller as Controller_keyboard

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as Bsoup

import random
import time
import os

from YCBA_webScrape import FillText

def DriverInst(webdriverDir, headless):
    if headless == True:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920x1080")

        
        driver = webdriver.Chrome(executable_path=webdriverDir, chrome_options=chrome_options)
    
    else:
        option = webdriver.ChromeOptions()
        # option.add_experimental_option("debuggerAddress", "localhost:9222")
        driver = webdriver.Chrome(executable_path=webdriverDir, chrome_options=option)
        driver.maximize_window() # For maximizing window
        # driver.implicitly_wait(20)
        driver.implicitly_wait(5)

    return driver

def STATIC(username, password, targetList):

    keyboard = Controller_keyboard()
    def checkLogin(username, password):
        # os.system('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\localhost')
        # os.system("cd ../../../../../")
        # os.system("cd 'C:\Program Files\Google\Chrome\Application'")
        # os.system('chrome.exe --remote-debugging-port=9222 "https://www.youtube.com/watch?v=OC5zHACynR4&list=RDMM&index=3" --user-data-dir="C:/Users/aidan/Dev_Files/Python/Projects/Jay/YCBA/tools/localhost"')
        
        # driver.get(f"https://www.youtube.com")
        driver.get(f"https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den-GB%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&hl=en-GB&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
        # btnSignIn = driver.find_element_by_css_selector("[aria-label='Sign in']")
        # print("btnSignIn:", btnSignIn)
        # btnSignIn.click()
        # username = "sid"
        
        FillText(username, 0.01, 1, 0, keyboard)
        FillText(password, 0.01, 3, 0, keyboard)

        # print(driver)
        check = driver.find_elements_by_xpath("//*[contains(text(), 'This browser or app may not be secure.')]")
        if check != []:
            return False
        else:
            return True

    def postComments(targetList, keyboard):
        # pass
        for link in targetList:
            driver.get(link)
            time.sleep(3)
            keyboard.press(Key.tab)
            keyboard.release(Key.tab)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            time.sleep(0.5)
            keyboard.press(Key.page_down)
            keyboard.release(Key.page_down)
            
            time.sleep(1)
            # elem = driver.find_elements_by_xpath("//*[@class='ytd-comment-simplebox-renderer' and @class='style-scope' and @id='simplebox-placeholder']")
            elem = driver.find_element_by_xpath("//*[contains(text(), 'Commenting publicly as ')]").click()
            # print(elem)

            FillText(commentContent(), 0.01, 2, 0, keyboard)

            time.sleep(400)

    
    def commentContent():


        content = """*
HI hellop peicop/give sad bs
NO bs *gogi* nneds perfo gonga
-_- -   -       -            -
"""
        return content
    
    # fileLocationPath = os.path.dirname(os.path.realpath(__file__))
    fileLocationPath = os.getcwd()

    # webdriverDir = f"{fileLocationPath}\\tools\\chromedriver.exe"
    webdriverDir = "C:/Users/aidan/Dev_Files/Python/Projects/Jay/YCBA/tools/chromedriver.exe"

    driver = DriverInst(webdriverDir, False)


    while True:

        loginPassed = checkLogin(username, password)

        if loginPassed == True:
            # pass
            # check if want to save user/pass
            postComments(targetList, keyboard)
        else:
            time.sleep(10)# new user/pass
            loginPassed = checkLogin(username, password)
        

    # driver.get(f"https://www.youtube.com")

    time.sleep(200) # aria-label
    
    # if driver.title == "404 Not Found":
    #     driver.get(f"https://www.youtube.com/user/{channelList[0]}/videos")
    #     time.sleep(1)
    #     if driver.title == "404 Not Found":
    #         return False

    # driver.quit()

if __name__ == "__main__":

    # STATIC("aidanmachue@gmail.com", "b", [])
    STATIC("acc.1.kjnscdqk.aekj.cnpowmxq.42.2021@gmail.com", "softmadperson", ["https://www.youtube.com/watch?v=UI7B-5TltMU", "https://www.youtube.com/watch?v=c-WUDqdPchg", "https://www.youtube.com/watch?v=ROy57arUE1s", "https://www.youtube.com/watch?v=2PudHraDfis", "https://www.youtube.com/watch?v=8fTG4JT9v3k", "https://www.youtube.com/watch?v=UUur8HyndNU", "https://www.youtube.com/watch?v=eLqFIMWvKO4", "https://www.youtube.com/watch?v=1hXjio24CJU", "https://www.youtube.com/watch?v=Qe1GNg_c3JI", "https://www.youtube.com/watch?v=L2BhBc46Fao", "https://www.youtube.com/watch?v=_PB_CZ8aogk", "https://www.youtube.com/watch?v=m8PILb6pHqw", "https://www.youtube.com/watch?v=VWLN2EjAGzM", "https://www.youtube.com/watch?v=7z5oH2ZTEi8", "https://www.youtube.com/watch?v=zCpWlulIOEs", "https://www.youtube.com/watch?v=r8hjfGhwK-c", "https://www.youtube.com/watch?v=1HuhUVkNlFo", "https://www.youtube.com/watch?v=2vh8xBHKDCw", "https://www.youtube.com/watch?v=-5ssX_CIlfw", "https://www.youtube.com/watch?v=zjdiXz3iWr8", "https://www.youtube.com/watch?v=gttWR9QOynY", "https://www.youtube.com/watch?v=y0V4oGpXcKk", "https://www.youtube.com/watch?v=eM0ip3KJpRg", "https://www.youtube.com/watch?v=9fpiuS81D8c", "https://www.youtube.com/watch?v=xdfHcLo7DPw", "https://www.youtube.com/watch?v=jlCMef-qeQw", "https://www.youtube.com/watch?v=75K_TpGmRWM", "https://www.youtube.com/watch?v=yjyE0sHGeVw", "https://www.youtube.com/watch?v=nLxK_2qh0ic", "https://www.youtube.com/watch?v=oGhId1eehSA", "https://www.youtube.com/watch?v=jLcwY3U7uuw", "https://www.youtube.com/watch?v=Xx_uq7a6DCk", "https://www.youtube.com/watch?v=bKf9I4vftFE", "https://www.youtube.com/watch?v=WVhJEi-VNgs", "https://www.youtube.com/watch?v=uEO0rMPjJq0", "https://www.youtube.com/watch?v=JbSKfvO8u_M", "https://www.youtube.com/watch?v=d6N77sXUAcA", "https://www.youtube.com/watch?v=--XHzecOzdU", "https://www.youtube.com/watch?v=QFq8GBH5zks", "https://www.youtube.com/watch?v=ot4bPtNmi9E", "https://www.youtube.com/watch?v=X64excKVLlo", "https://www.youtube.com/watch?v=li7oIWa9lng", "https://www.youtube.com/watch?v=pApfHrF5qP4", "https://www.youtube.com/watch?v=Jz_tvdJLnZs", "https://www.youtube.com/watch?v=Fgoo_eY-UI0", "https://www.youtube.com/watch?v=faj3ZQGKk6U", "https://www.youtube.com/watch?v=ceivdq-rcHg", "https://www.youtube.com/watch?v=9NV-ZbxBrUY", "https://www.youtube.com/watch?v=3CxZttGFGHI", "https://www.youtube.com/watch?v=HIfMMQ3QfBQ", "https://www.youtube.com/watch?v=oS8kwHoZBA0", "https://www.youtube.com/watch?v=maab9Vv5zqo", "https://www.youtube.com/watch?v=9r6uDAAL2D4", "https://www.youtube.com/watch?v=Mf6NCLMLQL8", "https://www.youtube.com/watch?v=-mfMozLJMp8", "https://www.youtube.com/watch?v=SK3ehQ2Z9VA", "https://www.youtube.com/watch?v=1zJOcHGw4Bo", "https://www.youtube.com/watch?v=-bohlrx9jzY", "https://www.youtube.com/watch?v=FjHGZj2IjBk", "https://www.youtube.com/watch?v=CXeDdq94yww", "https://www.youtube.com/watch?v=b-nl9hM5v9Q", "https://www.youtube.com/watch?v=rkGKWVleI58", "https://www.youtube.com/watch?v=u28r2f2O9GM", "https://www.youtube.com/watch?v=Wz-VMDG2CL4", "https://www.youtube.com/watch?v=ALqNPXo-vmI", "https://www.youtube.com/watch?v=iUploF6oHLI", "https://www.youtube.com/watch?v=fj1iVV-2w2Y", "https://www.youtube.com/watch?v=marpQKKSBDI", "https://www.youtube.com/watch?v=v34fOa7Fy00", "https://www.youtube.com/watch?v=QlgXietwpUM", "https://www.youtube.com/watch?v=hYUP3U3Z85g", "https://www.youtube.com/watch?v=wR2Y-fLavxA", "https://www.youtube.com/watch?v=uElVY3DqfhY", "https://www.youtube.com/watch?v=7VR6HiJ2Hio", "https://www.youtube.com/watch?v=5EID4Aoci34", "https://www.youtube.com/watch?v=62iv9pKzd-U", "https://www.youtube.com/watch?v=bPzADVMYfQs", "https://www.youtube.com/watch?v=79L0CbLl_Ag", "https://www.youtube.com/watch?v=Ynj3-BOmBrM", "https://www.youtube.com/watch?v=lN9VH-5h6Q8", "https://www.youtube.com/watch?v=eX685w9m4jg", "https://www.youtube.com/watch?v=lXCnBXwRePY", "https://www.youtube.com/watch?v=baSsQsv8Fgc", "https://www.youtube.com/watch?v=mJTvDlyw1R0", "https://www.youtube.com/watch?v=x_a9Myuu58w", "https://www.youtube.com/watch?v=vZ6FUUkJOPw", "https://www.youtube.com/watch?v=QAcdbMpEkmw", "https://www.youtube.com/watch?v=xhacQzAywa4", "https://www.youtube.com/watch?v=DR-xxUQCDEc", "https://www.youtube.com/watch?v=uhM0lxkglfE", "https://www.youtube.com/watch?v=LO4oB1Vdvp4", "https://www.youtube.com/watch?v=58MVgeUsKZA", "https://www.youtube.com/watch?v=fU272HaDj_Y", "https://www.youtube.com/watch?v=VBK65940ZYI", "https://www.youtube.com/watch?v=yRmU1TH5u9w", "https://www.youtube.com/watch?v=ODx2zwbl5qA", "https://www.youtube.com/watch?v=vr3Yw7lRHl8", "https://www.youtube.com/watch?v=x6zJ7kJ-AgA", "https://www.youtube.com/watch?v=QrJ3RI_5ykM", "https://www.youtube.com/watch?v=05OozaTZFLg", "https://www.youtube.com/watch?v=WdGzvKK7P7I", "https://www.youtube.com/watch?v=WJFCJkZKWeY", "https://www.youtube.com/watch?v=JIuRrjONEHg", "https://www.youtube.com/watch?v=esV3UEJk6mI", "https://www.youtube.com/watch?v=iL9MonAoTlE", "https://www.youtube.com/watch?v=73UVP3QDiYo", "https://www.youtube.com/watch?v=0T1v9VY4r1w", "https://www.youtube.com/watch?v=zBbA58sEUDo", "https://www.youtube.com/watch?v=jVgBvRHVNYU", "https://www.youtube.com/watch?v=N-J0AeZnjo4", "https://www.youtube.com/watch?v=UJ86VrbV7oA"])