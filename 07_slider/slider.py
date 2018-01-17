import sys
from PyQt5.QtWidgets import (QLineEdit, QSlider, QPushButton, QApplication, QWidget, QVBoxLayout)
from PyQt5.QtCore import Qt

class Window(QWidget):
	def __init__(self):
		super().__init__()
		self.init_ui()

	def init_ui(self):
		self.line_edit = QLineEdit()
		self.button1 = QPushButton("Clear")
		self.button2 = QPushButton("Print")
		self.slider = QSlider(Qt.Horizontal)
		self.slider.setMinimum(1)
		self.slider.setMaximum(99)
		self.slider.setValue(25)
		self.slider.setTickInterval(10)
		self.slider.setTickPosition(QSlider.TicksBelow)

		v_box = QVBoxLayout()
		v_box.addWidget(self.line_edit)
		v_box.addWidget(self.button1)
		v_box.addWidget(self.button2)
		v_box.addWidget(self.slider)

		self.setLayout(v_box)
		self.setWindowTitle("Slider")

		self.button1.clicked.connect(lambda: self.btn_click(self.button1, "henllo from clear btn"))
		self.button2.clicked.connect(lambda: self.btn_click(self.button2, "henllo from print btn"))
		self.slider.valueChanged.connect(self.v_change)

		self.show()

	def btn_click(self, button, string):
		if button.text() == "Print":
			print(self.line_edit.text())
		else:
			self.line_edit.clear()
		print(string)

	def v_change(self):
		aux_value = str(self.slider.value())
		self.line_edit.setText(aux_value)
		print(aux_value)


app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())