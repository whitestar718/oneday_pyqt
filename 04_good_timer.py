from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtCore import pyqtSignal
from threading import Thread
from PyQt6.QtCore import QTimer
import time
from datetime import datetime

form_window = uic.loadUiType("04_timer.ui")[0]

class UiMainWindow(QMainWindow, form_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button_pushed = False

        # button event handling
        self.pushButton.clicked.connect(self.click_slots)

        # thread headling
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time_text)
        self.timer.start(1000)
        self.show()
    
    @pyqtSlot()
    def click_slots(self):
        self.button_pushed = not self.button_pushed

    @pyqtSlot()
    def update_time_text(self):
        if self.button_pushed:
            nowtime = datetime.now()
            self.timeLabel.setText(nowtime.strftime("%H:%M:%S"))
        else:
            print("button not pushed")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = UiMainWindow()    
    sys.exit(app.exec())