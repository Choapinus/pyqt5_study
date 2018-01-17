import sys
from PyQt5.QtWidgets import (QLabel, QRadioButton, QPushButton, QVBoxLayout, QApplication, QWidget)

class Window(QWidget):
	def __init__(self):
		super().__init__()
		self.init_ui()

	def init_ui(self):
		self.setWindowTitle("RadioButton")

		self.label = QLabel("Which do you like best!!")
		self.dog = QRadioButton("Dogs")
		self.cat = QRadioButton("Cats")
		self.btn = QPushButton("Select")

		layout = QVBoxLayout()
		layout.addWidget(self.label)
		layout.addWidget(self.dog)
		layout.addWidget(self.cat)
		layout.addWidget(self.btn)

		self.setLayout(layout)

		self.btn.clicked.connect(lambda: self.btn_click(self.dog.isChecked(), self.label))

		self.show()

	def btn_click(self, check, lbl):
		if check:
			lbl.setText("I guess you like dogs")
		else:
			lbl.setText("So it's cats for yah boi")



app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())