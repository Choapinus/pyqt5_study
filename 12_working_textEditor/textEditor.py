import sys, os
from PyQt5.QtWidgets import (QApplication, QTextEdit, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog)


class Notepad(QWidget):

	def __init__(self):
		super(Notepad, self).__init__()
		self.text = QTextEdit(self)
		self.load_btn = QPushButton("Load")
		self.clear_btn = QPushButton("Clear")
		self.save_btn = QPushButton("Save")
		self.setWindowTitle("Save text from QEditText")

		self.init_ui()

	def init_ui(self):
		v_layout = QVBoxLayout()
		h_layout = QHBoxLayout()

		h_layout.addWidget(self.clear_btn)
		h_layout.addWidget(self.save_btn)
		h_layout.addWidget(self.load_btn)

		v_layout.addWidget(self.text)
		v_layout.addLayout(h_layout)

		self.setLayout(v_layout)

		self.clear_btn.clicked.connect(self.clear)
		self.save_btn.clicked.connect(lambda: self.text.clear())
		self.load_btn.clicked.connect(self.load)

		self.show()

	def load(self):
		filename = QFileDialog.getOpenFileName(self, "Open File", ".")
		print(filename)
		try:
			with open(filename[0], "r") as file:
				text = file.read()
				self.text.setText(text)
		except FileNotFoundError as err:
			print(err)

	def clear(self):
		# se puede agregar esto al connect del btn o una funcion lambda
		self.text.clear()

	def save(self):
		filename = QFileDialog.getSaveFileName(self, "Save File", ".", filter="Text File (*.txt)")
		print(filename)
		try:
			with open(filename[0], "w") as file:
				my_text = self.text.toPlainText()
				file.write(my_text)
		except FileNotFoundError:
			pass



app = QApplication(sys.argv)
writer = Notepad()
sys.exit(app.exec_())