import sys
from PyQt5.QtWidgets import (QLabel, QCheckBox, QPushButton, QVBoxLayout, QApplication, QWidget)


class Window(QWidget):
	def __init__(self):
		super().__init__()
		self.init_ui()

	def init_ui(self):
		self.label = QLabel()
		self.checkbox = QCheckBox("Do you like cats?")
		self.btn = QPushButton("Push me")

		layout = QVBoxLayout()
		layout.addWidget(self.label)
		layout.addWidget(self.checkbox)
		layout.addWidget(self.btn)

		self.setLayout(layout)
		self.setWindowTitle("CheckBox")

		self.btn.clicked.connect(lambda: self.btn_click(self.checkbox.isChecked(), self.label))

		self.show()

	def btn_click(self, chbox, lbl):
		if chbox == True:
			lbl.setText("I guess you like cats")
		else:
			lbl.setText("cats hater then")


app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
