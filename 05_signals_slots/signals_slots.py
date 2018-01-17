import sys
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):
	def __init__(self):
		# recordar que al heredar, debemos invocar el constructor de QWidget para
		# asi hacer uso de sus metodos (setWindowTittle y demases)
		super().__init__()
		self.init_ui()

	def init_ui(self):
		self.p_button = QtWidgets.QPushButton("Push me oe")
		self.label = QtWidgets.QLabel("I have not been changed yet")

		h_box = QtWidgets.QHBoxLayout()
		h_box.addStretch()
		h_box.addWidget(self.label)
		h_box.addStretch()

		v_box = QtWidgets.QVBoxLayout()
		v_box.addWidget(self.p_button)
		v_box.addLayout(h_box)

		self.setLayout(v_box)
		self.setWindowTitle("Signals & Slots")

		self.p_button.clicked.connect(self.btn_click) # se le pasa una funcion o:

		self.show()

	def btn_click(self):
		self.label.setText("me tocaste v:<")

app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())