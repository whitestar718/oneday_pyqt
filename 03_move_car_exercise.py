from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtCore import pyqtSignal

form_window = uic.loadUiType("03_move_car.ui")[0]

class UiMainWindow(QMainWindow, form_window):
    # ★★★★★ Signal (name: "start_signal")
    
    ##########################################################

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # button event handling
        self.button1.clicked.connect(self.clicked1)
        self.button2.clicked.connect(self.clicked2)
        self.button3.clicked.connect(self.clicked3)

        # clicked variable
        self.button1_clicked = False
        self.button2_clicked = False
        self.button3_clicked = False

        # ★★★★★ connect signl to slot ("start_signal" to "start_car")

        ##########################################################


        self.show()

    @pyqtSlot()
    def clicked1(self):
        if not self.button1_clicked:
            self.button1_value.setText("O")
            self.button1_value.setStyleSheet("color: green")
        else:
            self.button1_value.setText("X")
            self.button1_value.setStyleSheet("color: red")

        self.button1_clicked = not self.button1_clicked
        self.move()


    @pyqtSlot()
    def clicked2(self):
        if not self.button2_clicked:
            self.button2_value.setText("O")
            self.button2_value.setStyleSheet("color: green")
        else:
            self.button2_value.setText("X")
            self.button2_value.setStyleSheet("color: red")

        self.button2_clicked = not self.button2_clicked
        self.move()

    @pyqtSlot()
    def clicked3(self):
        if not self.button3_clicked:
            self.button3_value.setText("O")
            self.button3_value.setStyleSheet("color: green")
        else:
            self.button3_value.setText("X")
            self.button3_value.setStyleSheet("color: red")

        self.button3_clicked = not self.button3_clicked
        self.move()

    @pyqtSlot()
    def move(self):
        if self.button1_clicked and self.button2_clicked and self.button3_clicked:
            self.start_signal.emit(True)
        else:
            self.start_signal.emit(False)


    # ★★★★★ Slot (name: start_car)

    ##########################################################


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = UiMainWindow()    
    sys.exit(app.exec())