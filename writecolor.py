import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QBrush
from test import Ui_MainWindow


app = QApplication(sys.argv)

MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)



class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 350, 100)
        self.setWindowTitle('Colours')
        self.show()



    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()


    def drawRectangles(self, qp):

        try:

            filefind = open('color.txt')
            filefind = filefind.readlines()

            filefind = filefind[0]


            Redcolor = int(filefind[0: filefind.find(';')])
            Bluecolor = int(filefind[filefind.find(';') + 1: filefind.find(':')])
            Greencolor = int(filefind[filefind.find(':') + 1: filefind.find('.')])
            Transparency = int(filefind[filefind.find('.') + 1:])

        except:

            fileadd = open('color.txt', 'w')
            Redcolor = Bluecolor = Greencolor = 0
            Transparency = 255
            
            fileadd.write(str(Redcolor) + ';')
            fileadd.write(str(Bluecolor) + ':')
            fileadd.write(str(Greencolor) + '.')
            fileadd.write(str(Transparency))

            


        col = QColor(Redcolor, Bluecolor, Greencolor, Transparency)
        col.setNamedColor('#d4d4d4')
        qp.setPen(col)

        col = QColor(Redcolor, Bluecolor, Greencolor, Transparency)

        qp.setBrush(col)
        qp.drawRect(10, 15, 90, 60)











