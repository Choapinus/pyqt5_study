import sys
from PyQt5 import QtWidgets

def window():
	app = QtWidgets.QApplication(sys.argv)
	#size = (app.desktop().screenGeometry().width(), app.desktop().screenGeometry().height()) #get width and height from desktop
	w = QtWidgets.QWidget()
	button1 = QtWidgets.QPushButton(w) # creamos un boton pasando el widget en el que estara
	label1 = QtWidgets.QLabel(w) # creamos un label pasando el widget en el que estara
	button1.setText("Presioname oie x:") # seteamos texto del boton
	label1.setText("Noticeame senpai") # seteamos texto del label
	button1.move(100, 50) # movemos el boton para que no quede encima del label
	label1.move(110, 100) # movemos el label para que no quede encima del boton
	w.setWindowTitle("Buttons and Events") # seteamos titulo
	w.setGeometry(100, 100, 300, 200)
	w.show()
	sys.exit(app.exec_())

window()