import sys
from PyQt5.QtWidgets import (QApplication, QTextEdit, QWidget, QPushButton, QVBoxLayout)


class Notepad(QWidget):

	def __init__(self):
		super(Notepad, self).__init__()
		self.text = QTextEdit(self)
		self.clear_btn = QPushButton("Clear")
		self.save_btn = QPushButton("Save")
		self.setWindowTitle("Save text from QEditText")

		self.init_ui()

	def init_ui(self):
		layout = QVBoxLayout()
		layout.addWidget(self.text)
		layout.addWidget(self.save_btn)
		layout.addWidget(self.clear_btn)

		self.setLayout(layout)

		self.clear_btn.clicked.connect(self.clear)
		self.save_btn.clicked.connect(self.save)

		self.show()

	def clear(self):
		self.text.clear()

	def save(self):
		with open("output.txt", "w") as file:
			my_text = self.text.toPlainText()
			file.write(my_text)



app = QApplication(sys.argv)
writer = Notepad()
sys.exit(app.exec_())