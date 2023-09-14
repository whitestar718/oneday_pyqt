from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import pyqtSlot

form_window = uic.loadUiType("02_button_event.ui")[0]

class UiMainWindow(QMainWindow, form_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # button event handling
        self.click_me.clicked.connect(self.clicked)

        self.show()

    def print_hello_world(self):
        print(self.hello_world_text.text())

    @pyqtSlot()
    def clicked(self):
        self.hello_world_text.setText("clicked.. amazing...")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = UiMainWindow()
    
    window.print_hello_world()
    sys.exit(app.exec())

    