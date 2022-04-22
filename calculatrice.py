from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

# number input

# some error


#
def af0():
    ch = win.led.text()
    win.led.setText(ch+'0')


def af1():
    ch = win.led.text()
    win.led.setText(ch+'1')


def af2():
    ch = win.led.text()
    win.led.setText(ch+'2')


def af3():
    ch = win.led.text()
    win.led.setText(ch+'3')


def af4():
    ch = win.led.text()
    win.led.setText(ch+'4')


def af5():
    ch = win.led.text()
    win.led.setText(ch+'5')


def af6():
    ch = win.led.text()
    win.led.setText(ch+'6')


def af7():
    ch = win.led.text()
    win.led.setText(ch+'7')


def af8():
    ch = win.led.text()
    win.led.setText(ch+'8')


def af9():
    ch = win.led.text()
    win.led.setText(ch+'9')
# calculatrice inside fonction


def plus1():
    ch = win.res.text()
    ch1 = win.led.text()
    ch2 = ch + ch1+"+"
    win.ero.clear()
    if ch2[0] == "+":
        ch2 = ch2[1:]
        win.ero.setText("you cant put it at the first ")

    win.res.setText(ch2)
    win.led.clear()
    win.bplus.hide()
    win.bnega.hide()
    win.bsur.hide()
    win.bfoi.hide()


def moi1():
    ch = win.res.text()
    ch1 = win.led.text()
    ch2 = ch + ch1+"-"

    win.ero.clear()

    win.led.clear()
    if ch2[0] != "-":
        win.bplus.hide()
        win.bnega.hide()
        win.bsur.hide()
        win.bfoi.hide()

    if ch2.find("--") != -1:
        win.ero.setText("you can't put -- ")
    else:
        win.res.setText(ch2)


def sur():
    ch = win.res.text()
    ch1 = win.led.text()
    ch2 = ch + ch1+"/"
    win.ero.clear()
    if ch2[0] == "/":
        ch2 = ch2[1:]
        win.ero.setText("you cant put it at the first ")

    win.res.setText(ch2)
    win.led.clear()
    win.led.clear()
    win.bplus.hide()
    win.bnega.hide()
    win.bsur.hide()
    win.bfoi.hide()


def foi():
    ch = win.res.text()
    ch1 = win.led.text()
    ch2 = ch + ch1+"*"
    win.ero.clear()
    if ch2[0] == "*":
        ch2 = ch2[1:]
        win.ero.setText("you cant put it at the first ")

    win.res.setText(ch2)
    win.led.clear()
    win.led.clear()
    win.bplus.hide()
    win.bnega.hide()
    win.bsur.hide()
    win.bfoi.hide()

# calculater other fonction


def eface():
    ch = win.res.text()
    ch1 = ch[:len(ch)-1]
    win.res.setText(ch1)
    if (ch1.find("+") or ch1.find("*") or ch1.find("-") or ch1.find("/")) == -1:
        win.bplus.show()
        win.bnega.show()
        win.bsur.show()
        win.bfoi.show()


def efface():
    win.led.clear()
    win.res.clear()
    win.ero.clear()
    win.bplus.show()
    win.bnega.show()
    win.bsur.show()
    win.bfoi.show()


def quite():
    win.close()


def egal():
    x = win.res.text()
    x1 = int(x[1:len(x)-1])
    x2 = int(x[:len(x)-1])
    y = win.led.text()
    win.led.clear()
    r = 0
    if x[0] == "-":
        if x[len(x)-1] == "+":
            r = -x1+int(y)
        elif x[len(x)-1] == "-":
            r = -x1-int(y)
        elif x[len(x)-1] == "*":
            r = -x1*int(y)
        elif x[len(x)-1] == "/":
            r = -x1/int(y)
        else:
            win.res.clear()
            win.ero.setText("unspected error")
    else:
        if x[len(x)-1] == "+":
            r = x2+int(y)
        elif x[len(x)-1] == "-":
            r = x2-int(y)
        elif x[len(x)-1] == "*":
            r = x2*int(y)
        elif x[len(x)-1] == "/":
            r = x2/int(y)
        else:
            win.res.clear()
            win.ero.setText("unspected error")

    win.res.setText(str(r))
    win.bplus.show()
    win.bnega.show()
    win.bsur.show()
    win.bfoi.show()


app = QApplication([])
win = loadUi("calculatrice.ui")
win.show()
win.bclear.clicked.connect(efface)
win.bexit.clicked.connect(quite)
win.b0.clicked.connect(af0)
win.b1.clicked.connect(af1)
win.b2.clicked.connect(af2)
win.b3.clicked.connect(af3)
win.b4.clicked.connect(af4)
win.b5.clicked.connect(af5)
win.b6.clicked.connect(af6)
win.b7.clicked.connect(af7)
win.b8.clicked.connect(af8)
win.b9.clicked.connect(af9)
win.bplus.clicked.connect(plus1)
win.bnega.clicked.connect(moi1)
win.bfoi.clicked.connect(foi)
win.bsur.clicked.connect(sur)
win.befa.clicked.connect(eface)
win.bega.clicked.connect(egal)
app.exec_()
