# напиши здесь код третьего экрана приложения
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout 
from PyQt5.QtCore import Qt
from instr import *

class FinalWin(QWidget):
    def __init__(self, age, test1, test2, test3):
        super().__init__()
        self.age = int(age)
        self.test1 = test1
        self.test2 = test2
        self.test3 = test3
        self.set_appear()
        self.initUI()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.workheart = QLabel(txt_workheart + self.results())
        self.index = QLabel(txt_index + str(self.index))
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.index, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.workheart, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)
    def results(self):
        self.index = (4*(int(self.test1)+int(self.test2)+int(self.test3))-200)/10
        if self.age >= 15:
            if self.index >= 15:
                return txt_res1
            elif self.index >= 11 and self.index < 15:
                return txt_res2
            elif self.index >= 6 and self.index < 11:
                return txt_res3
            elif self.index >= 0.5 and self.index < 6:
                return txt_res4
            else: return txt_res5
        elif self.age == 13 or self.age == 14:
            if self.index >= 16.5:
                return txt_res1
            elif self.index >= 12.5 and self.index < 16.5:
                return txt_res2
            elif self.index >= 7.5 and self.index < 12.5:
                return txt_res3
            elif self.index >= 2 and self.index < 7.5:
                return txt_res4
            else: return txt_res5
        elif self.age == 11 or self.age == 12:
            if self.index >= 18:
                return txt_res1
            elif self.index >= 14 and self.index < 18:
                return txt_res2
            elif self.index >= 9 and self.index < 14:
                return txt_res3
            elif self.index >= 3.5 and self.index < 9:
                return txt_res4
            else: return txt_res5
        elif self.age == 9 or self.age == 10:
            if self.index >= 19.5:
                return txt_res1
            elif self.index >= 15.5 and self.index < 19.5:
                return txt_res2
            elif self.index >= 10.5 and self.index < 15.5:
                return txt_res3
            elif self.index >= 5 and self.index < 10.5:
                return txt_res4
            else: return txt_res5
        elif self.age == 7 or self.age == 8:
            if self.index >= 21:
                return txt_res1
            elif self.index >= 17 and self.index < 21:
                return txt_res2
            elif self.index >= 12 and self.index < 17:
                return txt_res3
            elif self.index >= 6.5 and self.index < 12:
                return txt_res4
            else: return txt_res5
        else:
            return 'Вы ещё слишком молод(а) для данного теста.'