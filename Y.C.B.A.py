import win32gui, win32con

hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide, win32con.SW_HIDE)

from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui, uic, QtTest
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys
import time
# import os

import random

import json

from YCBA_webScrape import STATIC
from YCBA_webScrape import ListProcessing
# from YCBA_RR import STATIC

# def run():
#     for i in range(10):
#         print(i)


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

    def opacity(self, start, target, duration, widget, reverse):

        self.effect = QGraphicsOpacityEffect()
        widget.setGraphicsEffect(self.effect)

        self.anim = QtCore.QPropertyAnimation(self.effect, b"opacity")
        self.anim.setStartValue(start)
        
        Animate.animate(self, target, duration)

        if reverse == True:
            self.anim = QtCore.QPropertyAnimation(self.effect, b"opacity")
            self.anim.setStartValue(target)
            Animate.animate(self, start, duration)

    pass



def jsonStore(location, data):
    with open(location, 'w') as file:  #open the file in write mode
        json.dump(data, file)   # json.dump() function to stores the set of numbers in numbers.json file



class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.show()

        uic.loadUi("resources/splash.ui", self)

        # self.creditLabel.clicked.connect(STATIC())

        self.anim_loading()

        uic.loadUi("resources/splashToMenu.ui", self)
        Animate.position(self, QPoint(0, -20), 3000, self.titleLabel)

        uic.loadUi("resources/menu.ui", self)
        self.btnManage.setStyleSheet("QPushButton { background-color: qlineargradient(spread:pad, x1:0.448, y1:0, x2:0.507, y2:1, stop:0 rgba(109, 93, 189, 0), stop:1 rgba(23, 17, 80, 0)); border-radius: 20px; color: rgb(123, 105, 213, 0); }")
        self.btnGet.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.448, y1:0, x2:0.507, y2:1, stop:0 rgba(109, 93, 189, 0), stop:1 rgba(23, 17, 80, 0)); border-radius: 20px; color: rgb(123, 105, 213, 0);")
        self.btnExe.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.448, y1:0, x2:0.507, y2:1, stop:0 rgba(109, 93, 189, 0), stop:1 rgba(23, 17, 80, 0)); border-radius: 20px; color: rgb(123, 105, 213, 0);")

        for w in [self.btnManage, self.btnGet, self.btnExe]:
            Animate.opacity(self, 0, 0, 00, w, False)

        self.btnManage.setStyleSheet("QPushButton { background-color: qlineargradient(spread:pad, x1:0.448, y1:0, x2:0.507, y2:1, stop:0 rgba(109, 93, 189, 255), stop:1 rgba(23, 17, 80, 255)); border-radius: 20px; color: rgb(123, 105, 213); }")
        self.btnGet.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.448, y1:0, x2:0.507, y2:1, stop:0 rgba(109, 93, 189, 255), stop:1 rgba(23, 17, 80, 255)); border-radius: 20px; color: rgb(123, 105, 213);")
        self.btnExe.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.448, y1:0, x2:0.507, y2:1, stop:0 rgba(109, 93, 189, 255), stop:1 rgba(23, 17, 80, 255)); border-radius: 20px; color: rgb(123, 105, 213);")

        Animate.opacity(self, 0, 1, 500, self.btnManage, False)
        Animate.opacity(self, 0, 1, 500, self.btnGet, False)
        Animate.opacity(self, 0, 1, 1500, self.btnExe, False)

        self.btnManage.clicked.connect(self.click_btnManage)
        self.btnGet.clicked.connect(self.click_btnGet)
        self.btnExe.clicked.connect(self.click_btnExe)

    def click_btnManage(self):
        Animate.opacity(self, 1, 0.8, 70, self.btnManage, True)
        STATIC()

    def click_btnGet(self):
        Animate.opacity(self, 1, 0.8, 70, self.btnGet, True)
        videoLinks = STATIC()
        jsonStore("vLinks_all.json", videoLinks)
        videoLinks = ListProcessing(videoLinks, 3)
        jsonStore("vLinks.json", videoLinks)

    
    def click_btnExe(self):
        Animate.opacity(self, 1, 0.8, 70, self.btnExe, True)
        STATIC()
    
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

        # app=QApplication(sys.argv)
        # UIWindow = UI()
        # app.exec_()

        # time.sleep(5)
        # print("dddd")
        # uic.loadUi("resources/splash_89.ui", self)
        
#         # self.browse.clicked.connect(self.browsefiles)

app=QApplication(sys.argv)
UIWindow = UI()
app.exec_()
# print("end")
#     # def browsefiles(self):
#     #     fname=QFileDialog.getOpenFileName(self, 'Open file', 'D:\codefirst.io\PyQt5 tutorials\Browse Files', 'Images (*.png, *.xmp *.jpg)')
#     #     self.filename.setText(fname[0])


# mainwindow=QMainWindow()
# widget=QtWidgets.QStackedWidget() 
# widget.addWidget(mainwindow)
# widget.setFixedWidth(680)
# widget.setFixedHeight(400)
# widget.show()
# sys.exit(app.exec_())