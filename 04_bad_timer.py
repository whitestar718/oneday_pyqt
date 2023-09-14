from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtCore import pyqtSignal
from threading import Thread
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
        Thread(target=self.time_loop, daemon=True).start()
        self.show()

    def time_loop(self):
        while True:
            if self.button_pushed:
                nowtime = datetime.now()
                self.timeLabel.setText(nowtime.strftime("%H:%M:%S"))
            else:
                pass
            time.sleep(0.5)
    
    @pyqtSlot()
    def click_slots(self):
        self.button_pushed = not self.button_pushed

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = UiMainWindow()    
    sys.exit(app.exec())