from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import time
import random
import os
import sys

import MyComponents.WidgetMachine as SlotM


class MyImageViewerWidget(QFrame):
    def __init__(self, *args):
        super(MyImageViewerWidget, self).__init__(*args)
        self.setGeometry(0, 0, 800, 600)
        self.ui = SlotM.Ui_Form()
        self.ui.setupUi(self)
        self.cpt = 0

        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(ROOT_DIR, "slot_machine_symbols.png")
        self.px = QPixmap(path)

        self.x = [0, 0, 0, 300, 300, 300, 600, 600, 600]
        self.y = [0, 300, 600, 0, 300, 600, 0, 300, 600]
        self.timer = QTimer()

        rect = QRect(0, 0, 300, 300)
        cropped = self.px.copy(rect)
        self.ui.mLabel.setPixmap(cropped)
        self.ui.mLabel2.setPixmap(cropped)
        self.ui.mLabel3.setPixmap(cropped)

        self.timer = QTimer()
        self.timer.start(7000)
        self.timer.timeout.connect(self.spin)

    def spin(self):
        for i in range(0, 20):
            time.sleep((50 + 25 * i) / 1000)

            c = random.randint(0, len(self.x) - 1)

            self.rect = QRect(self.x[c], self.y[c], 300, 300)
            cropped = self.px.copy(self.rect)
            self.ui.mLabel3.setPixmap(cropped)

            if i < 10:
                a = random.randint(0, len(self.x) - 1)
                self.rect = QRect(self.x[a], self.y[a], 300, 300)
                cropped = self.px.copy(self.rect)
                self.ui.mLabel.setPixmap(cropped)

            if i < 15:
                b = random.randint(0, len(self.x) - 1)
                self.rect = QRect(self.x[b], self.y[b], 300, 300)
                cropped = self.px.copy(self.rect)
                self.ui.mLabel2.setPixmap(cropped)
            QApplication.processEvents()

        self.cpt += 1
        if a == b and c == b:
            print("===============")
            print("=== JACKPOT ===")
            print("===============")

        else:
            print("game over, " + str(self.cpt) + " games played")


class MyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)

        # attributs de la fenetre principale
        self.setGeometry(500, 450, 940, 320)
        self.setFixedSize(940, 320)
        self.setWindowTitle('Slot Machine')

        self.mDisplay = MyImageViewerWidget(self)

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Space:
            self.mDisplay.spin()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyMainWindow()
    w.show()
    app.exec_()
