import virtualkeyboard as vkb

from PyQt6.QtWidgets import QLabel, QMainWindow, QListWidget, QVBoxLayout, QWidget
from PyQt6 import QtWidgets
import sys

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.mainWidget = QWidget()
        self.lo = QVBoxLayout()
        self.label = QLabel()
        self.list = QListWidget()
        self.list.itemClicked.connect(self.btnQClicked)
#        self.list.clicked.connect(self.btnQClicked)
        self.lo.addWidget(self.label)
        self.lo.addWidget(self.list)
        self.mainWidget.setLayout(self.lo)
        self.list.addItems(["hej", "å", "hå", "ssid", "ett annat ssid"])
        self.setGeometry(0, 0, 900, 400)
        self.setWindowTitle('Virtual Keyboard')
        self.setCentralWidget(self.mainWidget)
        self.show()

        return

    def btnQClicked(self):

        self.kbd = vkb.Kbd(self)
        self.label.setText(self.kbd.text)
        return
    

#def main():
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec())
