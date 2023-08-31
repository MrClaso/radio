from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QDialog
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QFont

class Kbd(QDialog):

    def __init__(self, parent = None):
        super(Kbd, self).__init__(parent)
        self.text = ""
        self.initUI()

    def initUI(self):
        self.capsOn = False
        self.numOn = False

        self.kbd = QWidget(self)
        self.kbd.setFont(QFont('Arial', 50))
        self.textArea = QLabel()
        self.row1 = QHBoxLayout()
        self.row2 = QHBoxLayout()
        self.row3 = QHBoxLayout()
        self.rows = QVBoxLayout()
        self.rows.addWidget(self.textArea)
        self.rows.addLayout(self.row1)
        self.rows.addLayout(self.row2)
        self.rows.addLayout(self.row3)
        self.kbd.setLayout(self.rows)

        self.letterSize = QSize(60,90)
        self.capsSize = QSize(105,90)

        self.btnq = QPushButton("q")
        self.btnq.clicked.connect(self.btnQClicked)
        self.btnq.setFixedSize(self.letterSize)
        self.row1.addWidget(self.btnq)
        self.btnw = QPushButton("w")
        self.btnw.clicked.connect(self.btnWClicked)
        self.btnw.setFixedSize(self.letterSize)
        self.row1.addWidget(self.btnw)
        self.btne = QPushButton("e")
        self.btne.clicked.connect(self.btnEClicked)
        self.btne.setFixedSize(self.letterSize)
        self.row1.addWidget(self.btne)
        self.btnr = QPushButton("r")
        self.btnr.clicked.connect(self.btnRClicked)
        self.btnr.setFixedSize(self.letterSize)
        self.row1.addWidget(self.btnr)
        self.btnt = QPushButton("t")
        self.btnt.clicked.connect(self.btnTClicked)
        self.btnt.setFixedSize(self.letterSize)
        self.row1.addWidget(self.btnt)
        self.btny = QPushButton("y")
        self.btny.clicked.connect(self.btnYClicked)
        self.btny.setFixedSize(self.letterSize)
        self.row1.addWidget(self.btny)
        self.btnu = QPushButton("u")
        self.btnu.clicked.connect(self.btnUClicked)
        self.btnu.setFixedSize(self.letterSize)
        self.row1.addWidget(self.btnu)
        self.btni = QPushButton("i")
        self.btni.clicked.connect(self.btnIClicked)
        self.btni.setFixedSize(self.letterSize)
        self.row1.addWidget(self.btni)
        self.btno = QPushButton("o")
        self.btno.clicked.connect(self.btnOClicked)
        self.btno.setFixedSize(self.letterSize)
        self.row1.addWidget(self.btno)
        self.btnp = QPushButton("p")
        self.btnp.clicked.connect(self.btnPClicked)
        self.btnp.setFixedSize(self.letterSize)
        self.row1.addWidget(self.btnp)
        self.btnBsp = QPushButton()
        self.btnBsp.clicked.connect(self.btnBspClicked)
        self.btnBsp.setFixedSize(self.capsSize)
        self.btnBsp.setIconSize(QSize(60,60))
        self.btnBsp.setIcon(QIcon("/Users/clasostman/Development/pyqt/bsp.png"))
        self.row1.addWidget(self.btnBsp)

        self.btnCaps = QPushButton()
        self.btnCaps.setFixedSize(self.capsSize)
        self.btnCaps.setIconSize(QSize(60,60))
        self.btnCaps.setIcon(QIcon("/Users/clasostman/Development/pyqt/caps.png"))
        self.btnCaps.clicked.connect(self.toggleCaps)
        self.row2.addWidget(self.btnCaps)
        self.btna = QPushButton("a")
        self.btna.clicked.connect(self.btnAClicked)
        self.btna.setFixedSize(self.letterSize)
        self.row2.addWidget(self.btna)
        self.btns = QPushButton("s")
        self.btns.clicked.connect(self.btnSClicked)
        self.btns.setFixedSize(self.letterSize)
        self.row2.addWidget(self.btns)
        self.btnd = QPushButton("d")
        self.btnd.clicked.connect(self.btnDClicked)
        self.btnd.setFixedSize(self.letterSize)
        self.row2.addWidget(self.btnd)
        self.btnf = QPushButton("f")
        self.btnf.clicked.connect(self.btnFClicked)
        self.btnf.setFixedSize(self.letterSize)
        self.row2.addWidget(self.btnf)
        self.btng = QPushButton("g")
        self.btng.clicked.connect(self.btnGClicked)
        self.btng.setFixedSize(self.letterSize)
        self.row2.addWidget(self.btng)
        self.btnh = QPushButton("h")
        self.btnh.clicked.connect(self.btnHClicked)
        self.btnh.setFixedSize(self.letterSize)
        self.row2.addWidget(self.btnh)
        self.btnj = QPushButton("j")
        self.btnj.clicked.connect(self.btnJClicked)
        self.btnj.setFixedSize(self.letterSize)
        self.row2.addWidget(self.btnj)
        self.btnk = QPushButton("k")
        self.btnk.clicked.connect(self.btnKClicked)
        self.btnk.setFixedSize(self.letterSize)
        self.row2.addWidget(self.btnk)
        self.btnl = QPushButton("l")
        self.btnl.clicked.connect(self.btnLClicked)
        self.btnl.setFixedSize(self.letterSize)
        self.row2.addWidget(self.btnl)

        self.num = QPushButton("?123")
        self.num.clicked.connect(self.toggleNumeric)
        self.num.setFixedSize(QSize(130,90))
        self.row3.addWidget(self.num)
        self.btnz = QPushButton("z")
        self.btnz.clicked.connect(self.btnZClicked)
        self.btnz.setFixedSize(self.letterSize)
        self.row3.addWidget(self.btnz)
        self.btnx = QPushButton("x")
        self.btnx.clicked.connect(self.btnXClicked)
        self.btnx.setFixedSize(self.letterSize)
        self.row3.addWidget(self.btnx)
        self.btnc = QPushButton("c")
        self.btnc.clicked.connect(self.btnCClicked)
        self.btnc.setFixedSize(self.letterSize)
        self.row3.addWidget(self.btnc)
        self.btnv = QPushButton("v")
        self.btnv.clicked.connect(self.btnVClicked)
        self.btnv.setFixedSize(self.letterSize)
        self.row3.addWidget(self.btnv)
        self.btnb = QPushButton("b")
        self.btnb.clicked.connect(self.btnBClicked)
        self.btnb.setFixedSize(self.letterSize)
        self.row3.addWidget(self.btnb)
        self.btnn = QPushButton("n")
        self.btnn.clicked.connect(self.btnNClicked)
        self.btnn.setFixedSize(self.letterSize)
        self.row3.addWidget(self.btnn)
        self.btnm = QPushButton("m")
        self.btnm.clicked.connect(self.btnMClicked)
        self.btnm.setFixedSize(self.letterSize)
        self.row3.addWidget(self.btnm)
        self.btnRight = QPushButton()
        self.btnRight.clicked.connect(self.btnRightClicked)
        self.btnRight.setFixedSize(self.capsSize)
        self.btnRight.setIconSize(QSize(60,60))
        self.btnRight.setIcon(QIcon("/Users/clasostman/Development/pyqt/right.png"))
        self.row3.addWidget(self.btnRight)

        self.setGeometry(0, 0, 900, 400)
        self.setWindowTitle('Virtual Keyboard')
        self.exec()
        return

    def toggleCaps(self):
        if self.numOn:
            return
        
        if self.capsOn:
            self.btna.setText("a")
            self.btnb.setText("b")
            self.btnc.setText("c")
            self.btnd.setText("d")
            self.btne.setText("e")
            self.btnf.setText("f")
            self.btng.setText("g")
            self.btnh.setText("h")
            self.btni.setText("i")
            self.btnj.setText("j")
            self.btnk.setText("k")
            self.btnl.setText("l")
            self.btnm.setText("m")
            self.btnn.setText("n")
            self.btno.setText("o")
            self.btnp.setText("p")
            self.btnq.setText("q")
            self.btnr.setText("r")
            self.btns.setText("s")
            self.btnt.setText("t")
            self.btnu.setText("u")
            self.btnv.setText("v")
            self.btnw.setText("w")
            self.btnx.setText("x")
            self.btny.setText("y")
            self.btnz.setText("z")
        else:
            self.btna.setText("A")
            self.btnb.setText("B")
            self.btnc.setText("C")
            self.btnd.setText("D")
            self.btne.setText("E")
            self.btnf.setText("F")
            self.btng.setText("G")
            self.btnh.setText("H")
            self.btni.setText("I")
            self.btnj.setText("J")
            self.btnk.setText("K")
            self.btnl.setText("L")
            self.btnm.setText("M")
            self.btnn.setText("N")
            self.btno.setText("O")
            self.btnp.setText("P")
            self.btnq.setText("Q")
            self.btnr.setText("R")
            self.btns.setText("S")
            self.btnt.setText("T")
            self.btnu.setText("U")
            self.btnv.setText("V")
            self.btnw.setText("W")
            self.btnx.setText("X")
            self.btny.setText("Y")
            self.btnz.setText("Z")
        self.capsOn = not self.capsOn
        return
    
    def toggleNumeric(self):
        if self.numOn:
            self.btna.setText("a")
            self.btnb.setText("b")
            self.btnc.setText("c")
            self.btnd.setText("d")
            self.btne.setText("e")
            self.btnf.setText("f")
            self.btng.setText("g")
            self.btnh.setText("h")
            self.btni.setText("i")
            self.btnj.setText("j")
            self.btnk.setText("k")
            self.btnl.setText("l")
            self.btnm.setText("m")
            self.btnn.setText("n")
            self.btno.setText("o")
            self.btnp.setText("p")
            self.btnq.setText("q")
            self.btnr.setText("r")
            self.btns.setText("s")
            self.btnt.setText("t")
            self.btnu.setText("u")
            self.btnv.setText("v")
            self.btnw.setText("w")
            self.btnx.setText("x")
            self.btny.setText("y")
            self.btnz.setText("z")
        else:
            self.btna.setText("@")
            self.btnb.setText(";")
            self.btnc.setText("'")
            self.btnd.setText("$")
            self.btne.setText("2")
            self.btnf.setText("_")
            self.btng.setText("&&")
            self.btnh.setText("-")
            self.btni.setText("7")
            self.btnj.setText("+")
            self.btnk.setText("(")
            self.btnl.setText("/")
            self.btnm.setText("?")
            self.btnn.setText("!")
            self.btno.setText("8")
            self.btnp.setText("9")
            self.btnq.setText("0")
            self.btnr.setText("3")
            self.btns.setText("#")
            self.btnt.setText("4")
            self.btnu.setText("6")
            self.btnv.setText(":")
            self.btnw.setText("1")
            self.btnx.setText('"')
            self.btny.setText("5")
            self.btnz.setText("*")

        self.numOn = not self.numOn
        self.capsOn = False
        return


    def btnBspClicked(self):
        self.text = self.text[:-1]
        self.textArea.setText(self.text)
        return
    
    def btnQClicked(self):
        if self.numOn:
            self.text += "0"
        elif self.capsOn:
            self.text += "Q"
        else:
            self.text += "q"   
        self.textArea.setText(self.text)     
        return

    def btnWClicked(self):
        if self.numOn:
            self.text += "1"
        elif self.capsOn:
            self.text += "W"
        else:
            self.text += "w"   
        self.textArea.setText(self.text)     
        return

    def btnEClicked(self):
        if self.numOn:
            self.text += "2"
        elif self.capsOn:
            self.text += "E"
        else:
            self.text += "e"   
        self.textArea.setText(self.text)     
        return

    def btnRClicked(self):
        if self.numOn:
            self.text += "3"
        elif self.capsOn:
            self.text += "R"
        else:
            self.text += "r"   
        self.textArea.setText(self.text)     
        return

    def btnTClicked(self):
        if self.numOn:
            self.text += "4"
        elif self.capsOn:
            self.text += "T"
        else:
            self.text += "t"   
        self.textArea.setText(self.text)     
        return

    def btnYClicked(self):
        if self.numOn:
            self.text += "5"
        elif self.capsOn:
            self.text += "Y"
        else:
            self.text += "y"   
        self.textArea.setText(self.text)     
        return

    def btnUClicked(self):
        if self.numOn:
            self.text += "6"
        elif self.capsOn:
            self.text += "U"
        else:
            self.text += "u"   
        self.textArea.setText(self.text)     
        return

    def btnIClicked(self):
        if self.numOn:
            self.text += "7"
        elif self.capsOn:
            self.text += "I"
        else:
            self.text += "i"   
        self.textArea.setText(self.text)     
        return

    def btnOClicked(self):
        if self.numOn:
            self.text += "8"
        elif self.capsOn:
            self.text += "O"
        else:
            self.text += "o"   
        self.textArea.setText(self.text)     
        return

    def btnPClicked(self):
        if self.numOn:
            self.text += "9"
        elif self.capsOn:
            self.text += "P"
        else:
            self.text += "p"   
        self.textArea.setText(self.text)     
        return

    def btnAClicked(self):
        if self.numOn:
            self.text += "@"
        elif self.capsOn:
            self.text += "A"
        else:
            self.text += "a"   
        self.textArea.setText(self.text)     
        return

    def btnSClicked(self):
        if self.numOn:
            self.text += "#"
        elif self.capsOn:
            self.text += "S"
        else:
            self.text += "s"   
        self.textArea.setText(self.text)     
        return

    def btnDClicked(self):
        if self.numOn:
            self.text += "$"
        elif self.capsOn:
            self.text += "D"
        else:
            self.text += "d"   
        self.textArea.setText(self.text)     
        return

    def btnFClicked(self):
        if self.numOn:
            self.text += "_"
        elif self.capsOn:
            self.text += "F"
        else:
            self.text += "f"   
        self.textArea.setText(self.text)     
        return

    def btnGClicked(self):
        if self.numOn:
            self.text += "&"
        elif self.capsOn:
            self.text += "G"
        else:
            self.text += "g"   
        self.textArea.setText(self.text)     
        return

    def btnHClicked(self):
        if self.numOn:
            self.text += "-"
        elif self.capsOn:
            self.text += "H"
        else:
            self.text += "h"   
        self.textArea.setText(self.text)     
        return

    def btnJClicked(self):
        if self.numOn:
            self.text += "+"
        elif self.capsOn:
            self.text += "J"
        else:
            self.text += "j"   
        self.textArea.setText(self.text)     
        return

    def btnKClicked(self):
        if self.numOn:
            self.text += "("
        elif self.capsOn:
            self.text += "K"
        else:
            self.text += "k"   
        self.textArea.setText(self.text)     
        return

    def btnLClicked(self):
        if self.numOn:
            self.text += "/"
        elif self.capsOn:
            self.text += "L"
        else:
            self.text += "l"   
        self.textArea.setText(self.text)     
        return

    def btnZClicked(self):
        if self.numOn:
            self.text += "*"
        elif self.capsOn:
            self.text += "Z"
        else:
            self.text += "z"   
        self.textArea.setText(self.text)     
        return

    def btnXClicked(self):
        if self.numOn:
            self.text += '"'
        elif self.capsOn:
            self.text += "X"
        else:
            self.text += "x"   
        self.textArea.setText(self.text)     
        return

    def btnCClicked(self):
        if self.numOn:
            self.text += "'"
        elif self.capsOn:
            self.text += "C"
        else:
            self.text += "c"   
        self.textArea.setText(self.text)     
        return

    def btnVClicked(self):
        if self.numOn:
            self.text += ":"
        elif self.capsOn:
            self.text += "V"
        else:
            self.text += "v"   
        self.textArea.setText(self.text)     
        return

    def btnBClicked(self):
        if self.numOn:
            self.text += ";"
        elif self.capsOn:
            self.text += "B"
        else:
            self.text += "b"   
        self.textArea.setText(self.text)     
        return

    def btnNClicked(self):
        if self.numOn:
            self.text += "!"
        elif self.capsOn:
            self.text += "N"
        else:
            self.text += "n"   
        self.textArea.setText(self.text)     
        return

    def btnMClicked(self):
        if self.numOn:
            self.text += "?"
        elif self.capsOn:
            self.text += "M"
        else:
            self.text += "m"   
        self.textArea.setText(self.text)     
        return

    def btnRightClicked(self):
        self.accept()

