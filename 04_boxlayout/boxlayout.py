import sys
from PyQt5 import QtWidgets

def window():
	app = QtWidgets.QApplication(sys.argv) #application
	w = QtWidgets.QWidget() #window
	button = QtWidgets.QPushButton("push me?")
	label = QtWidgets.QLabel("Look at me oe")
	#primero se crean los elementos que seran agregados al boxlayout

	w.setWindowTitle("Boxlayout") #se define titulo de la ventana

	h_box = QtWidgets.QHBoxLayout() #horizontal box
	h_box.addStretch() # agrega un espacio dentro de la ventana
	h_box.addWidget(label) # añadimos el label
	h_box.addStretch() # creamos otro espacio dentro de la ventana
	# dos espacios para que ambos queden centrados?

	"""
	# con esto quedan en la izquierda
	v_box = QtWidgets.QVBoxLayout() #se instancia VBoxLayout
	v_box.addWidget(button)
	v_box.addWidget(label)
	#se le añaden los elementos que seran agregados al VBoxLayout
	"""

	#con esto quedan centrados con el h_box
	v_box = QtWidgets.QVBoxLayout() #se instancia VBoxLayout
	v_box.addWidget(button)
	v_box.addLayout(h_box)

	w.setLayout(v_box)
	#se setea el Layout

	w.show() #mostramos la ventana

	sys.exit(app.exec_())

window()