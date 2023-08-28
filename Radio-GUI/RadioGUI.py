from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow, QGroupBox)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap, QFont
import sys
import json

#import board
#import busio
import time
#import adafruit_max9744

#import mpd

# Initialize I2C bus.
#i2c = busio.I2C(board.SCL, board.SDA)

# Initialize amplifier.
#amp = adafruit_max9744.MAX9744(i2c)
# Optionally you can specify a different addres if you override the AD1, AD2
# pins to change the address.
# amp = adafruit_max9744.MAX9744(i2c, address=0x49)

#client = mpd.MPDClient()
#client.connect("localhost", 6600)
path = "/Users/clasostman/Project/radio/Radio-GUI/"
f = open(path + "stations.json", "r")
j = f.read()
statlist = json.loads(j)

print(statlist)

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.volume = 34
#        amp.volume = self.volume    # Volume is a value from 0 to 63 where 0 is muted/off and
                                    # 63 is maximum volume.
        self.groupBox = QGroupBox()
        self.scroll = QScrollArea()             # Scroll Area which contains the radio stations push buttons
        self.scroll.setStyleSheet("background-color : black;")
        self.midWidget = QWidget()
        self.playingLayout = QVBoxLayout()
        self.volumeLabelLabel = QLabel("Volym")
        self.volumeLabelLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.volumeLabelLabel.setFont(QFont('Arial', 32))
        self.volumeLabel = QLabel()
        self.volumeLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.volumeLabel.setFont(QFont('Arial', 80))
        self.volumeLabel.setText("{}".format(self.volume))
        self.playingLabelLabel = QLabel("Du lyssnar på")
        self.playingLabelLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.playingLabelLabel.setFont(QFont("Arial", 24))
        self.playingLabel = QLabel()
        self.playingLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
#        self.playingLabel.setSize()
        self.playingLayout.addWidget(self.volumeLabelLabel)
        self.playingLayout.addWidget(self.volumeLabel)
        self.playingLayout.addWidget(self.playingLabelLabel)
        
        self.playingLayout.addWidget(self.playingLabel)
        self.midWidget.setLayout(self.playingLayout)
        self.rightWidget = QWidget()
        self.vbox = QVBoxLayout()               # The rows in scroll area
        self.hbox = QHBoxLayout()       
        self.mainWidget = QWidget()
        self.rightLayout = QVBoxLayout()
        self.hbox.addWidget(self.scroll)
        self.hbox.addWidget(self.midWidget)
        self.hbox.addWidget(self.rightWidget)
        self.hbox.setStretch(0, 4)
        self.hbox.setStretch(1, 4)
        self.hbox.setStretch(2, 2)
        i = 1
        for s in statlist["stations"]:
            self.pb = QPushButton("", self)
            self.pb.setObjectName(s["name"])
            self.pb.setFixedSize(150, 150)
            self.pb.clicked.connect(self.stationClicked)
            self.pb.setIcon(QIcon(path + s["icon"]))
            self.pb.setIconSize(QSize(150, 150))
        #    self.pb.setStyleSheet("background-image : url(" + path + s["icon"] + ");")
            if i%2 == 1:
                self.hStations = QHBoxLayout()
            self.hStations.addWidget(self.pb)
    
            if i%2 == 0 or i == len(statlist["stations"]):
                self.vbox.addLayout(self.hStations)

            i += 1
        self.groupBox.setLayout(self.vbox)
        self.scroll.setWidget(self.groupBox)

        #Scroll Area Properties
#        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
#        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)

        self.volUpButton = QPushButton()
        self.volUpButton.setObjectName("VolUp")
        self.volUpButton.setFixedSize(150, 150)
        self.volUpButton.setStyleSheet("background-image : url(" + path + "res/images/volUp.png);")
        self.volUpButton.clicked.connect(self.volUpClicked)

        self.volDownButton = QPushButton()
        self.volDownButton.setObjectName("VolDown")
        self.volDownButton.setFixedSize(150, 150)
        self.volDownButton.setStyleSheet("background-image : url(" + path + "res/images/volDown.png);")
        self.volDownButton.clicked.connect(self.volDownClicked)

        self.onOffButton = QPushButton()
        self.onOffButton.setObjectName("Onoff")
        self.onOffButton.setFixedSize(150, 150)
        self.onOffButton.setStyleSheet("background-image : url(" + path + "res/images/onOff.png);")
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
#        client.clear()
        match = next(obj for obj in statlist["stations"] if obj["name"] == btn.objectName())
        print(match["url"])
#        client.add(match["url"])
#        client.play()
        pixmap = QPixmap(path + match["icon"])
        self.playingLabel.setPixmap(pixmap)

    def volUpClicked(self):
        btn = self.sender()
        print("pressed {}".format(btn.objectName()))
        if self.volume < 63:
#            amp.volume_up()
            self.volume += 1
            self.volumeLabel.setText("{}".format(self.volume))

    def volDownClicked(self):
        btn = self.sender()
        print("pressed {}".format(btn.objectName()))
        if self.volume > 0:
#            amp.volume_down()
            self.volume -= 1
            self.volumeLabel.setText("{}".format(self.volume))

    def onOffClicked(self):
        btn = self.sender()
        print("pressed {}".format(btn.objectName()))
#        client.pause()

#def main():
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec())

#if __name__ == '__main__':
#    main()