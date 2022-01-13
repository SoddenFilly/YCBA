import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import * 
from PyQt5 import * 
# from PyQt5.QtWidgets import QDialogue, QApplication


class Ui_PageFirst(QMainWindow):    #Page1

    def __init__(self):
        super(Ui_PageFirst, self).__init__()
        loadUi("menu.ui", self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def changeToPage2(self):
        widget.setCurrentWidget(secondpage)

class Ui_PageSecond(QMainWindow):   #Page2
    def changeToPage1(self):
        widget.setCurrentWidget(firstpage)

app = QApplication(sys.argv)
widget = QStackedWidget()
#######
firstpage = Ui_PageFirst()
widget.addWidget(firstpage)   # create an instance of the first page class and add it to stackedwidget

secondpage = Ui_PageSecond() 
widget.addWidget(secondpage)   # adding second page

widget.setCurrentWidget(firstpage)   # setting the page that you want to load when application starts up. you can also use setCurrentIndex(int)
########
widget.show()
app.exec_()