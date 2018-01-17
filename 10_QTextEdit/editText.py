import sys
from PyQt5.QtWidgets import (QApplication, QTextEdit, QWidget, QPushButton, QVBoxLayout)


class Notepad(QWidget):

	def __init__(self):
		super(Notepad, self).__init__()
		self.text = QTextEdit(self)
		self.clear_btn = QPushButton("Clear")
		self.setWindowTitle("QEditText")

		self.init_ui()

	def init_ui(self):
		layout = QVBoxLayout()
		layout.addWidget(self.text)
		layout.addWidget(self.clear_btn)

		self.setLayout(layout)

		self.clear_btn.clicked.connect(self.clear)

		self.show()

	def clear(self):
		self.text.clear()



app = QApplication(sys.argv)
writer = Notepad()
sys.exit(app.exec_())