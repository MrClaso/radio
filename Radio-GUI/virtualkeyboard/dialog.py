import sys
from PyQt6 import QtCore, QtGui, QtWidgets

class Dialog(QtWidgets.QDialog):
    def __init__(self, val, parent=None):
        super(Dialog, self).__init__(parent)
        self.val = val
        self.initUI()

    def initUI(self):
        endButton = QtWidgets.QPushButton('OK')
        endButton.clicked.connect(self.on_clicked)
        lay = QtWidgets.QVBoxLayout(self)
        lay.addWidget(endButton)
        self.setWindowTitle(str(self.val))

    @QtCore.pyqtSlot()
    def on_clicked(self):
        self.val += 1
        self.accept()

def main(): 
    app = QtWidgets.QApplication(sys.argv)
    for i in range(10):
        ex = Dialog(i)
#        ex.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        if ex.exec() == QtWidgets.QDialog.accepted:
            print(ex.val)

if __name__ == '__main__':
    main()