import sys
from PyQt5 import QtWidgets

def window(): # ventana que se le pasara al event loop
	app = QtWidgets.QApplication(sys.argv) # app object que recibe las variables del sistema
	w = QtWidgets.QWidget() # top level window
	w.setWindowTitle("Titulo ventana") # le setea un titulo a la ventana
	w.show() # mostrar ventana 
	sys.exit(app.exec_()) # comenza el event loop y el exit recibe el evento exit de la app

window() # hacemos llamada a la funcion creada y se mostrara la ventana