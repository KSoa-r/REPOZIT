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

        self.l_line.addWidget(self.name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.starttest1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.starttest2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.starttest3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test3, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.timer, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.sendresults, alignment = Qt.AlignRight)

        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

    def timer_test(self):
        global time
        time = QTime(0, 1, 0)
        self.timer1 = QTimer()
        self.timer1.timeout.connect(self.timer1Event)
        self.timer1.start(1000)

    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.timer.setText(time.toString('hh:mm:ss'))
        self.timer.setFont(QFont('Times', 36, QFont.Bold))
        self.timer.setStyleSheet('color: rgb(0, 0, 0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer1.stop()

    def timer_sits(self):
        global time
        time = QTime(0, 0, 30)
        self.timer2 = QTimer()
        self.timer2.timeout.connect(self.timer2Event)
        self.timer2.start(1500)

    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.timer.setText(time.toString('hh:mm:ss')[6:8])
        self.timer.setFont(QFont('Times', 36, QFont.Bold))
        self.timer.setStyleSheet('color: rgb(0, 0, 0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer2.stop()

    def timer_final(self):
        global time
        time = QTime(0, 1, 0)
        self.timer3 = QTimer()
        self.timer3.timeout.connect(self.timer3Event)
        self.timer3.start(1000)

    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.timer.setText(time.toString('hh:mm:ss')[6:8])
        self.timer.setFont(QFont('Times', 36, QFont.Bold))
        if int(time.toString('hh:mm:ss')[6:8]) >= 45: self.timer.setStyleSheet('color: rgb(0, 255, 0)')
        elif int(time.toString('hh:mm:ss')[6:8]) <= 15: self.timer.setStyleSheet('color: rgb(0, 255, 0)')
        else: self.timer.setStyleSheet('color: rgb(0, 0, 0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer3.stop()

    def connects(self):
        self.sendresults.clicked.connect(self.next_click)
        self.starttest1.clicked.connect(self.timer_test)
        self.starttest2.clicked.connect(self.timer_sits)
        self.starttest3.clicked.connect(self.timer_final)

    def next_click(self):
        self.hide()
        self.final_win = FinalWin(self.line_age.text(), self.line_test1.text(), self.line_test2.text(), self.line_test3.text())