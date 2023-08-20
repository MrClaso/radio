from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow)
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QIcon, QPixmap
import sys
import json

import board
import busio
import time
import adafruit_max9744

import mpd

# Initialize I2C bus.
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize amplifier.
amp = adafruit_max9744.MAX9744(i2c)
# Optionally you can specify a different addres if you override the AD1, AD2
# pins to change the address.
# amp = adafruit_max9744.MAX9744(i2c, address=0x49)

client = mpd.MPDClient()
client.connect("localhost", 6600)
amp.volume = 34  # Volume is a value from 0 to 63 where 0 is muted/off and
# 63 is maximum volume.

path = "/home/pi/radio/Radio-GUI/"
f = open(path + "stations.json", "r")
j = f.read()
statlist = json.loads(j)

print(statlist)

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.scroll = QScrollArea()             # Scroll Area which contains the widgets, set as the centralWidget
        self.leftWidget = QWidget()                 # Widget that contains the rows of stations 
        self.midWidget = QWidget()
        self.rightWidget = QWidget()
        self.vbox = QVBoxLayout()               # The Vertical Box that contains the Horizontal Boxes of  labels and buttons
        self.hbox = QHBoxLayout()
        self.mainWidget = QWidget()
        self.rightLayout = QVBoxLayout()
        self.hbox.addWidget(self.leftWidget)
        self.hbox.addWidget(self.midWidget)
        self.hbox.addWidget(self.rightWidget)

        i = 1
        for s in statlist["stations"]:
            self.pb = QPushButton("", self)
            self.pb.setObjectName(s["name"])
            self.pb.setFixedSize(150, 150)
            self.pb.clicked.connect(self.stationClicked)
            self.pb.setStyleSheet("background-image : url(" + path + s["icon"] + ");")
            if i%3 == 1:
                self.hStations = QHBoxLayout()
            self.hStations.addWidget(self.pb)
    
            if i%3 == 0 or i == len(statlist["stations"]):
                self.vbox.addLayout(self.hStations)

            i += 1

        self.leftWidget.setLayout(self.vbox)

        #Scroll Area Properties
#        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.leftWidget)

        self.volUpButton = QPushButton()
        self.volUpButton.setObjectName("VolUp")
        self.volUpButton.setFixedSize(150, 150)
        self.volUpButton.setStyleSheet("background-image : url(/home/pi/radio/Radio-GUI/res/images/volUp.png);")
        self.volUpButton.clicked.connect(self.volUpClicked)

        self.volDownButton = QPushButton()
        self.volDownButton.setObjectName("VolDown")
        self.volDownButton.setFixedSize(150, 150)
        self.volDownButton.setStyleSheet("background-image : url(/home/pi/radio/Radio-GUI/res/images/volDown.png);")
        self.volDownButton.clicked.connect(self.volDownClicked)

        self.onOffButton = QPushButton()
        self.onOffButton.setObjectName("Onoff")
        self.onOffButton.setFixedSize(150, 150)
        self.onOffButton.setStyleSheet("background-image : url(/home/pi/radio/Radio-GUI/res/images/onOff.png);")
#        self.onOffButton.setIcon(QIcon(QPixmap("/home/pi/radio/Radio-GUI/res/images/onOff.png)")))
#        self.onOffButton.setIconSize(QSize(150, 150));
        self.onOffButton.clicked.connect(self.onOffClicked)

        self.rightLayout.addWidget(self.onOffButton)
        self.rightLayout.addWidget(self.volUpButton)
        self.rightLayout.addWidget(self.volDownButton)
        self.rightWidget.setLayout(self.rightLayout)


        self.mainWidget.setLayout(self.hbox)
        self.setCentralWidget(self.mainWidget)

        self.setGeometry(0, 0, 1024, 600)
        self.setWindowTitle('RadioGUI')
        self.show()

        return


    # action method
    def stationClicked(self):
        btn = self.sender()
        # printing pressed
        print("pressed {}".format(btn.objectName()))
        client.clear()
        match = next(obj for obj in statlist["stations"] if obj["name"] == btn.objectName())
        print(match["url"])
        client.add(match["url"])
        client.play()

    def volUpClicked(self):
        btn = self.sender()
        print("pressed {}".format(btn.objectName()))
        amp.volume_up()

    def volDownClicked(self):
        btn = self.sender()
        print("pressed {}".format(btn.objectName()))
        amp.volume_down()

    def onOffClicked(self):
        btn = self.sender()
        print("pressed {}".format(btn.objectName()))
        client.pause()

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()