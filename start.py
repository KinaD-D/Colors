from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from writecolor import Example
from test import Ui_MainWindow
from PyQt5.QtGui import QColor, QPainter, QPaintDevice, QBrush
from PyQt5.QtWidgets import QFrame

app = QtWidgets.QApplication(sys.argv)

MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
ex = Example()
ex.show()



def RetrayColor():



	Redcolor = ui.spinBox.value()
	Bluecolor = ui.spinBox_2.value()
	Greencolor = ui.spinBox_3.value()
	Transparency = ui.verticalSlider.value()
	fileadd = open('color.txt', 'w')
	
	fileadd.write(str(Redcolor) + ';')
	fileadd.write(str(Greencolor) + ':')
	fileadd.write(str(Bluecolor) + '.')
	fileadd.write(str(Transparency))

	ex.close()

	ex.show()



ui.pushButton.clicked.connect(RetrayColor)

sys.exit(app.exec_())