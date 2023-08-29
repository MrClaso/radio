from virtualkeyboard import virtualkeyboard as vkb
#from import virtualkeyboard as vkb
import macwifi

from PyQt6.QtWidgets import QLabel, QMainWindow, QListWidget, QVBoxLayout, QWidget, QPushButton
from PyQt6 import QtWidgets
import sys

class SSIDWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        lines = macwifi.list().splitlines()
        self.ssidList = []
        for a in lines:
            self.ssidList.append(a.strip().split(" ")[0])

        self.mainWidget = QWidget(self)
        self.lo = QVBoxLayout()
        self.label = QLabel()
        self.list = QListWidget()
        self.list.itemClicked.connect(self.SSIDClicked)
        self.btnConnect = QPushButton("Anslut")
        self.btnConnect.clicked.connect(self.btnConnectClicked)
        self.lo.addWidget(self.label)
        self.lo.addWidget(self.list)
        self.lo.addWidget(self.btnConnect)
        self.mainWidget.setLayout(self.lo)
        self.list.addItems(self.ssidList)
        self.setGeometry(0, 0, 900, 400)
        self.setWindowTitle('Anslut till wifi')
#        self.setCentralWidget(self.mainWidget)
        self.show()
        return

    def SSIDClicked(self):

        self.kbd = vkb.Kbd(self)
        self.label.setText(self.kbd.text)
        return

    def btnConnectClicked(self):
# TODO Anslut till wifi
        self.close()
        return   

