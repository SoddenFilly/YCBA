from pynput import keyboard as klis
from pynput.keyboard import Key, Controller

import time

key_latest = ["null", "null"]
inputList = []

def Logger():


    def on_press(key):
        global key_latest
        global inputList
        key_latest = [key, True]
        # 

        # print(inputList)

        inputList.reverse()

        try:
            index_press = inputList.index([key, "P"])
        except:
            index_press = -1

        try:
            index_release = inputList.index([key, "R"])
        except:
            index_release = -1

        inputList.reverse()

        if [key, "P"] not in inputList:
            print("============")
            print(inputList)
            inputList.append([key, "P"])
            
            print(inputList)
            print("============")
        
        if [key, "R"] not in inputList:

            index_release = index_press - 1

        
        elif index_release <= index_press:

            print(index_press, index_release)

            inputList.append([key, "P"])

        # if [key, "P"] not in inputList:
        #     inputList.append([key, "P"])
        #     # print("hdhdhdhdhdhdh")
        # print(index_)


        # print(inputList)

        try:
            print('alphanumeric key {0} pressed'.format(
                key))
        except AttributeError:
            print('special key {0} pressed'.format(
                key))

    def on_release(key):
        global key_latest
        global inputList
        key_latest = [key, False]
        inputList.append([key, "R"])

        print('{0} released'.format(
            key))
        if key == klis.Key.esc:
            # Stop listener
            return False

    # ...or, in a non-blocking fashion:
    listener = klis.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()

    holdingMenu = False
    while True:
        # print(key_latest[0])
        time.sleep(1)

        if key_latest[0] == klis.Key.menu and key_latest[1] == True and holdingMenu == False:
            print("skjdcksckakjcs")
            holdingMenu = True

        print(inputList)
        print(time.time())


def Player():

    keyboard = Controller()

    time.sleep(5)

    def execute(commands):

        cList = commands.split("_")

        print(len(cList)/3)

        for c in range(int(len(cList)/3)):

            action = cList[c*3]
            key    = cList[c*3+1]
            delay  = cList[c*3+2]

            if action == "PR":
                keyboard.press(key)
                keyboard.release(key)
            elif action == "P":
                keyboard.press(key)
            elif action == "R":
                keyboard.release(key)

            time.sleep(float(delay))



    execute("PR_ _2_P_w_0.4_P_a_0.1_R_w_0_R_a_0")


# Logger()
Player()

keyboard = Controller()
keyboard.press("a")
time.sleep(2)
keyboard.release("a")