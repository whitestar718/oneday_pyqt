from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMainWindow

form_window = uic.loadUiType("01_hello_world.ui")[0]

class UiMainWindow(QMainWindow, form_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

    def print_hello_world(self):
        print(self.hello_world_text.text())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = UiMainWindow()
    
    window.print_hello_world()
    sys.exit(app.exec())

    