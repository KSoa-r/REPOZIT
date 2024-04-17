from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit, QHBoxLayout
from instr import *
from final_win import *

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.h_line = QHBoxLayout()
        self.l_line = QVBoxLayout()
        self.r_line = QVBoxLayout()

        self.name = QLabel(txt_name)
        self.line_name = QLineEdit(txt_hintname)
        self.age = QLabel(txt_age)
        self.line_age = QLineEdit(txt_hintage)
        self.test1 = QLabel(txt_test1)
        self.starttest1 = QPushButton(txt_starttest1)
        self.line_test1 = QLineEdit(txt_hinttest1)
        self.test2 = QLabel(txt_test2)
        self.starttest2 = QPushButton(txt_starttest2)
        self.line_test2 = QLineEdit(txt_hinttest2)
        self.test3 = QLabel(txt_test3)
        self.starttest3 = QPushButton(txt_starttest3)
        self.line_test3 = QLineEdit(txt_hinttest3)
        self.timer = QLabel(txt_timer)
        self.sendresults = QPushButton(txt_sendresults)

        self.l_line.addWidget(self.name, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.line_name, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.age, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.line_age, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.test1, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.starttest1, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.line_test1, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.test2, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.starttest2, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.line_test2, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.test3, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.starttest3, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.line_test3, alignment = Qt.AlignCenter)
        self.r_line.addWidget(self.timer, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.sendresults, alignment = Qt.AlignCenter)

        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
    
    def connects(self):
        self.sendresults.clicked.connects(self.next_click)

    def next_click(self):
        self.hide()
        self.final_win = FinalWin()

# app = QApplication([])
# window = TestWin()
# app.exec_()