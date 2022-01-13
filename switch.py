import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import * 
# from PyQt5.QtWidgets import QDialogue, QApplication

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("menu.ui", self)


class Screen2(QMainWindow):
    def __init__(self):
        super(Screen2, self).__init__()
        loadUi("ManageChannels.ui", self)



app = QApplication(sys.argv)

window = MainWindow()
app.exec_()

# try:
#     sys.exit(app.exec_())
# except:
#     print("Exiting")