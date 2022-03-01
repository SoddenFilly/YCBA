import win32gui, win32con # Provides access to much of the Win32 API etc
import sys
import time
import random
import threading
import json
import os

# For GUI
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui, uic, QtTest
from PyQt5.QtGui import * 
from PyQt5.QtCore import *

from YCBA_webScrape import STATIC as STATIC_WS, ListProcessing
from YCBA_CWriteBot import STATIC as STATIC_BT

with open("debugSettings.txt", "r") as text:
    debugSettings = text.readlines()

class Animate:
    def __init__(self):
        pass

    def animate(self, target, duration):
        
        self.anim.setEndValue(target)
        self.anim.setDuration(duration)
        self.anim.start()
        QtTest.QTest.qWait(duration)

    def value(self, target, duration, widget):
        
        self.anim = QPropertyAnimation(widget, b"value")
        self.anim.setEasingCurve(QEasingCurve.InOutCubic)

        Animate.animate(self, target, duration)

    def position(self, target, duration, widget):

        self.anim = QPropertyAnimation(widget, b"pos")
        self.anim.setEasingCurve(QEasingCurve.InOutCubic)
        
        Animate.animate(self, target, duration)

    def opacity(self, widget, start=1, target=0.8, duration=70, reverse=True):

        self.effect = QGraphicsOpacityEffect()
        widget.setGraphicsEffect(self.effect)

        self.anim = QtCore.QPropertyAnimation(self.effect, b"opacity")
        self.anim.setStartValue(start)
        
        Animate.animate(self, target, duration)

        if reverse == True:
            self.anim = QtCore.QPropertyAnimation(self.effect, b"opacity")
            self.anim.setStartValue(target)
            Animate.animate(self, start, duration)

def jsonStore(location, data):
    with open(location, 'w') as file:
        json.dump(data, file)

def getChannelNames(channel_list):
    
    # channel_list = "".join(channel_list)
    string = ""
    for ch in channel_list:
        string = string + ",\n" + ch
        print(string)
    return string[2:]

class StartupScene(QMainWindow):
    def __init__(self):
        super(StartupScene, self).__init__()

        self.channel_list = ["EddievanderMeer", "monoman", "PaulDavids"]#, "AKSTARENG", "SteveTerreberry", "PirateCrabUK", "CharlesBerthoud"]

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.show()

        self.fileLocationPath = os.path.dirname(os.path.realpath(__file__))

        # uic.loadUi(self.fileLocationPath+"/resources/splash.ui", self)
        uic.loadUi("resources/splash.ui", self)
        self.btnQuitProg.clicked.connect(self.click_btnQuitProg)
        self.btnSecret.clicked.connect(self.click_btnSecret)
        self.anim_loading()

        # uic.loadUi(self.fileLocationPath+"/resources/splashToMenu.ui", self)
        uic.loadUi("resources/splashToMenu.ui", self)
        self.btnQuitProg.clicked.connect(self.click_btnQuitProg)
        self.btnSecret.clicked.connect(self.click_btnSecret)
        Animate.position(self, QPoint(0, -20), 3000, self.titleLabel)

    def click_btnQuitProg(self):
        sys.exit()

    def click_btnSecret(self):
        STATIC_WS(secret=True)

    def anim_loading(self):

        ranges = [[0,0],[0,0],[0,0],[0,0],[0,0]]
        cap = 30

        for i in range(5):
            target = random.randint(10 + ranges[i][0], cap + ranges[i][1])
            duration = random.randint(1000, 3000)

            if target > 100:
                target = 100

            Animate.value(self, target, duration, self.progressBar)

            if target == 100:
                QtTest.QTest.qWait(1500)
                break

            try:
                ranges[i+1][0] = target
                cap = cap + ranges[i][1]
                ranges[i+1][1] = cap
                # print(target, cap)
            except:
                pass

class MainScene(QMainWindow):
    def __init__(self):
        super(MainScene, self).__init__()

        self.channel_list = ["monoman"] #, "EddievanderMeer", "PaulDavids"]#, "AKSTARENG", "SteveTerreberry", "PirateCrabUK", "CharlesBerthoud"]

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.show()

        self.fileLocationPath = os.path.dirname(os.path.realpath(__file__))
        
        # uic.loadUi(self.fileLocationPath+"/resources/menu.ui", self)
        uic.loadUi("resources/menu.ui", self)
        self.btnQuitProg.clicked.connect(self.click_btnQuitProg)
        self.btnSecret.clicked.connect(self.click_btnSecret)

        self.frame_3.hide()
        self.btnExeCancel.hide()
        self.btnExeConfirm.hide()

        self.btnManage.setStyleSheet("QPushButton { background-color: qlineargradient(spread:pad, x1:0.448, y1:0, x2:0.507, y2:1, stop:0 rgba(109, 93, 189, 0), stop:1 rgba(23, 17, 80, 0)); border-radius: 20px; color: rgb(123, 105, 213, 0); }")
        self.btnGet.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.448, y1:0, x2:0.507, y2:1, stop:0 rgba(109, 93, 189, 0), stop:1 rgba(23, 17, 80, 0)); border-radius: 20px; color: rgb(123, 105, 213, 0);")
        self.btnExe.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.448, y1:0, x2:0.507, y2:1, stop:0 rgba(109, 93, 189, 0), stop:1 rgba(23, 17, 80, 0)); border-radius: 20px; color: rgb(123, 105, 213, 0);")

        for w in [self.btnManage, self.btnGet, self.btnExe]:
            Animate.opacity(self, w, 0, 0, 0, False)

        self.btnManage.setStyleSheet("QPushButton { background-color: qlineargradient(spread:pad, x1:0.448, y1:0, x2:0.507, y2:1, stop:0 rgba(109, 93, 189, 255), stop:1 rgba(23, 17, 80, 255)); border-radius: 20px; color: rgb(123, 105, 213); }")
        Animate.opacity(self, self.btnManage, 0, 1, 500, False)

        self.btnGet.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.448, y1:0, x2:0.507, y2:1, stop:0 rgba(109, 93, 189, 255), stop:1 rgba(23, 17, 80, 255)); border-radius: 20px; color: rgb(123, 105, 213);")
        Animate.opacity(self, self.btnGet, 0, 1, 500, False)
        
        # # self.btnExe.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.448, y1:0, x2:0.507, y2:1, stop:0 rgba(109, 93, 189, 255), stop:1 rgba(23, 17, 80, 255)); border-radius: 20px; color: rgb(123, 105, 213);")
        # self.btnExe.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.448, y1:0, x2:0.507, y2:1, stop:0 rgba(109, 93, 189, 100), stop:1 rgba(23, 17, 80, 100)); border-radius: 20px; color: rgb(123, 105, 213, 100);")
        # if os.path.isfile(self.fileLocationPath+"/vLinks_targeted.json") == False:
        if os.path.isfile("data/vLinks_targeted.json") == False:
            self.btnExe.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.448, y1:0, x2:0.507, y2:1, stop:0 rgba(109, 93, 189, 100), stop:1 rgba(23, 17, 80, 100)); border-radius: 20px; color: rgb(123, 105, 213, 100);")
        else:
            self.btnExe.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.448, y1:0, x2:0.507, y2:1, stop:0 rgba(109, 93, 189), stop:1 rgba(23, 17, 80)); border-radius: 20px; color: rgb(123, 105, 213);")
            self.btnExe.clicked.connect(self.click_btnExe)
        Animate.opacity(self, self.btnExe, 0, 1, 1000, False)

        self.btnManage.clicked.connect(self.click_btnManage)
        self.btnGet.clicked.connect(self.click_btnGet)

        self.btnStatistics.clicked.connect(self.click_btnStatistics)
        self.btnSettings.clicked.connect(self.click_btnSettings)

        self.channelIsValidating = False

    def click_btnSettings(self):
        Animate.opacity(self, self.btnSettings)
        # UIWindow = UI()

    def click_btnStatistics(self):
        Animate.opacity(self, self.btnStatistics)
        
    def click_btnQuitProg(self):
        sys.exit()

    def click_btnSecret(self):
        STATIC_WS(secret=True)

    def click_btnManage(self):
        Animate.opacity(self, self.btnManage)
        # uic.loadUi(self.fileLocationPath+"/resources/ManageChannels.ui", self)
        uic.loadUi("resources/ManageChannels.ui", self)

        self.ChannelList.setPlainText(getChannelNames(self.channel_list))
        self.btnReturn.clicked.connect(self.click_btnReturn)

        self.fieldChannel.textChanged.connect(lambda: self.startThread("a"))

        self.btnAdd.clicked.connect(self.addChannel)
        self.btnRemove.clicked.connect(self.removeChannel)

    def addChannel(self):
        Animate.opacity(self, self.btnAdd)
        if self.fieldChannel.text() not in self.channel_list:
            self.channel_list.append(self.fieldChannel.text())
            self.ChannelList.setPlainText(getChannelNames(self.channel_list))
    
    def removeChannel(self):
        Animate.opacity(self, self.btnRemove)
        if self.fieldChannel.text() in self.channel_list:
            self.channel_list.remove(self.fieldChannel.text())
            self.ChannelList.setPlainText(getChannelNames(self.channel_list))

    def checkIfChannelExists(self):

        while True:
            print("Checking...")
            
            self.channelIsValidLabel_text = "Checking channel validity..."
            self.channelIsValidLabel_color = "color: rgb(220, 220, 220);"
            self.labelError.setText(self.channelIsValidLabel_text)
            self.labelError.setStyleSheet(self.channelIsValidLabel_color)
            
            # print(self.fieldChannel.text())
            isValid = STATIC_WS(channelList=[self.fieldChannel.text()], getVids=False, validateChannel=True)
            print(isValid)

            print("ssss", self.channelIsValid_updated)
            if self.channelIsValid_updated == False:
                # self.channelIsValid_updated = True

                if isValid == False:
                    self.labelError.setText("This channel name is not Valid")
                    self.labelError.setStyleSheet("color: rgb(255, 0, 80);")
                else:
                    self.labelError.setText("This channel name is Valid")
                    self.labelError.setStyleSheet("color: rgb(0, 255, 100);")
                
                self.channelIsValidating = False

                break
            else:
                self.channelIsValid_updated = False



        # if isValid == False:
        #     self.channelIsValidLabel_text = "This channel name is not Valid"
        #     self.channelIsValidLabel_color = "color: rgb(255, 0, 80);"
        # else:
        #     self.channelIsValidLabel_text = "This channel name is Valid"
        #     self.channelIsValidLabel_color = "color: rgb(0, 255, 100);"

        # self.channelValid_LabelUpdate()


    def channelValid_LabelUpdate(self):

        # self.labelError.setText(self.channelIsValidLabel_text)
        # self.labelError.setStyleSheet(self.channelIsValidLabel_color)

        


        pass

    def click_btnReturn(self):
        Animate.opacity(self, self.btnReturn)
        # uic.loadUi(self.fileLocationPath+"/resources/menu.ui", self)
        uic.loadUi("resources/menu.ui", self)
        self.btnQuitProg.clicked.connect(self.click_btnQuitProg)
        self.btnSecret.clicked.connect(self.click_btnSecret)

        self.frame_3.hide()
        self.btnExeCancel.hide()
        self.btnExeConfirm.hide()

        self.btnManage.clicked.connect(self.click_btnManage)
        self.btnGet.clicked.connect(self.click_btnGet)

        self.btnStatistics.clicked.connect(self.click_btnStatistics)
        self.btnSettings.clicked.connect(self.click_btnSettings)

        # if os.path.isfile(self.fileLocationPath+"/vLinks_targeted.json") == False:
        if os.path.isfile("data/vLinks_targeted.json") == False:
            self.btnExe.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.448, y1:0, x2:0.507, y2:1, stop:0 rgba(109, 93, 189, 100), stop:1 rgba(23, 17, 80, 100)); border-radius: 20px; color: rgb(123, 105, 213, 100);")
        else:
            self.btnExe.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.448, y1:0, x2:0.507, y2:1, stop:0 rgba(109, 93, 189), stop:1 rgba(23, 17, 80)); border-radius: 20px; color: rgb(123, 105, 213);")
            self.btnExe.clicked.connect(self.click_btnExe)

    def click_btnGet(self):
        Animate.opacity(self, self.btnGet)
        try:
            videoLinks = STATIC_WS(getVids=True, validateChannel=False, channelList=self.channel_list)
            if videoLinks == -1:
                return
                
            # jsonStore(self.fileLocationPath+"/vLinks_all.json", videoLinks)
            jsonStore("data/vLinks_all.json", videoLinks)
            videoLinks = ListProcessing(videoLinks, 3)
            # jsonStore(self.fileLocationPath+"/vLinks_targeted.json", videoLinks)
            jsonStore("data/vLinks_targeted.json", videoLinks)
        except:
            pass

        # if os.path.isfile(self.fileLocationPath+"/vLinks_targeted.json") == False:
        if os.path.isfile("data/vLinks_targeted.json") == False:
            self.btnExe.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.448, y1:0, x2:0.507, y2:1, stop:0 rgba(109, 93, 189, 100), stop:1 rgba(23, 17, 80, 100)); border-radius: 20px; color: rgb(123, 105, 213, 100);")
        else:
            self.btnExe.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.448, y1:0, x2:0.507, y2:1, stop:0 rgba(109, 93, 189), stop:1 rgba(23, 17, 80)); border-radius: 20px; color: rgb(123, 105, 213);")
            self.btnExe.clicked.connect(self.click_btnExe)

    def click_btnExe(self):
        Animate.opacity(self, self.btnExe)

        self.frame_3.show()
        self.btnExeCancel.show()
        self.btnExeConfirm.show()

        self.btnExeCancel.clicked.connect(self.click_btnExeCancel)
        self.btnExeConfirm.clicked.connect(self.click_btnExeConfirm)

    def click_btnExeCancel(self):
        Animate.opacity(self, self.btnExeCancel)

        self.frame_3.hide()
        self.btnExeCancel.hide()
        self.btnExeConfirm.hide()

    def click_btnExeConfirm(self):
        Animate.opacity(self, self.btnExeConfirm)

    def anim_loading(self):

        ranges = [[0,0],[0,0],[0,0],[0,0],[0,0]]
        cap = 30

        for i in range(5):
            target = random.randint(10 + ranges[i][0], cap + ranges[i][1])
            duration = random.randint(1000, 3000)

            if target > 100:
                target = 100

            Animate.value(self, target, duration, self.progressBar)

            if target == 100:
                QtTest.QTest.qWait(1500)
                break

            try:
                ranges[i+1][0] = target
                cap = cap + ranges[i][1]
                ranges[i+1][1] = cap
                # print(target, cap)
            except:
                pass

    def startThread(self, target):
        # print("ddskhjbcjdshbcsda", target)
        # for thread in threading.enumerate(): 
        #     print(thread.ident)
        # print(threading.get_ident())

        thread = threading.Thread(target=self.checkIfChannelExists)

        if self.channelIsValidating == False:
            self.channelIsValidating = True
            self.channelIsValid_updated = False

            self.channelIsValidLabel_text = "Checking channel validity..."
            self.channelIsValidLabel_color = "color: rgb(220, 220, 220);"

            

            thread.start()
        
        else:
            print("still validating")
            self.channelIsValid_updated = True

            # thread.start()




# class StartupScene(QMainWindow):
#     def __init__(self):
#         super(StartupScene, self).__init__()

#         self.channel_list = ["EddievanderMeer", "monoman", "PaulDavids"]#, "AKSTARENG", "SteveTerreberry", "PirateCrabUK", "CharlesBerthoud"]

#         self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
#         self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

#         self.show()

#         self.fileLocationPath = os.path.dirname(os.path.realpath(__file__))
        
#         if os.path.isfile("debug.mode") == True:
#             # uic.loadUi(self.fileLocationPath+"/resources/splash.ui", self)
#             uic.loadUi("resources/splash.ui", self)
#             self.btnQuitProg.clicked.connect(self.click_btnQuitProg)
#             self.btnSecret.clicked.connect(self.click_btnSecret)
#             self.anim_loading()

#             # uic.loadUi(self.fileLocationPath+"/resources/splashToMenu.ui", self)
#             uic.loadUi("resources/splashToMenu.ui", self)
#             self.btnQuitProg.clicked.connect(self.click_btnQuitProg)
#             self.btnSecret.clicked.connect(self.click_btnSecret)
#             Animate.position(self, QPoint(0, -20), 3000, self.titleLabel)

#     def click_btnQuitProg(self):
#         quit("\nQUIT\n")

#     def click_btnSecret(self):
#         STATIC(secret=True)

#     def anim_loading(self):

#         ranges = [[0,0],[0,0],[0,0],[0,0],[0,0]]
#         cap = 30

#         for i in range(5):
#             target = random.randint(10 + ranges[i][0], cap + ranges[i][1])
#             duration = random.randint(1000, 3000)

#             if target > 100:
#                 target = 100

#             Animate.value(self, target, duration, self.progressBar)

#             if target == 100:
#                 QtTest.QTest.qWait(1500)
#                 break

#             try:
#                 ranges[i+1][0] = target
#                 cap = cap + ranges[i][1]
#                 ranges[i+1][1] = cap
#                 # print(target, cap)
#             except:
#                 pass

if __name__ == "__main__":

    if "T" in debugSettings[0].split(":")[1]:
        hide = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(hide, win32con.SW_HIDE)

    app = QApplication(sys.argv)
    print(debugSettings[1].split(":")[1])
    if "F" in debugSettings[1].split(":")[1]:
        GUIWindow = StartupScene()
    GUIWindow = MainScene()

    app.exec_()