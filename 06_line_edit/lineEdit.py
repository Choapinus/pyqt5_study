import sys
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.init_ui()

	def init_ui(self):
		self.line_edit = QtWidgets.QLineEdit()
		self.button = QtWidgets.QPushButton("Clear")
		self.button2 = QtWidgets.QPushButton("Print")

		v_box = QtWidgets.QVBoxLayout()
		v_box.addWidget(self.line_edit)
		v_box.addWidget(self.button)
		v_box.addWidget(self.button2)

		self.setLayout(v_box)

		self.button.clicked.connect(self.btn_clicked)
		self.button2.clicked.connect(self.btn_clicked)


		self.setWindowTitle("Line Edit")

		self.show()

	def btn_clicked(self):
		sender = self.sender()
		if sender.text() == "Print":
			print(self.line_edit.text())
		else:
			self.line_edit.clear()



app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())