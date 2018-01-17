import sys
from PyQt5 import QtWidgets, QtGui

def window():
	app = QtWidgets.QApplication(sys.argv)
	w = QtWidgets.QWidget()
	label1 = QtWidgets.QLabel(w) # se le pasa el widget porque queremos que ese label este en esa ventana
	label2 = QtWidgets.QLabel(w)
	label1.setText("holi soy el label1 j3j3") # se le setea un texto
	label2.setPixmap(QtGui.QPixmap("doge.jpg")) # set pixmap setea una imagen y qtgui.qpixmap la carga
	label2.move(150, 40) # movemos la wea para que no quede encima del otro label
	w.setWindowTitle("Labels oezi")
	w.setGeometry(300, 300, 800, 600) # padding up, padding down, width, height => set ubication
	label1.move(130, 20) # move to x, y
	w.show()
	sys.exit(app.exec_())

window()