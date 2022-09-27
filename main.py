import math
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from functools import partial

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.flag_sub = False
        self.flag_sum = False
        self.flag_div = False
        self.flag_mul = False
        self.flag_sumf = False

        loader = QUiLoader()
        self.ui = loader.load('cal.ui', None)
        self.ui.show()
        self.btn_number_list = [self.ui.btn_0, self.ui.btn_1, self.ui.btn_2, self.ui.btn_3, self.ui.btn_4,
                                self.ui.btn_5, self.ui.btn_6, self.ui.btn_7, self.ui.btn_8, self.ui.btn_9]
        for i in range(10):
            self.btn_number_list[i].clicked.connect((partial(self.btn_numbers, i)))

    
        self.ui.plus_btn.clicked.connect(self.sum)
        self.ui.mul_btn.clicked.connect(self.mul)
        self.ui.div_btn.clicked.connect(self.div)
        self.ui.min_btn.clicked.connect(self.sub)
        self.ui.eq_btn.clicked.connect(self.equal)
        self.ui.clr_btn.clicked.connect(self.clear)
        self.ui.sin_btn.clicked.connect(self.sin)
        self.ui.cos_btn.clicked.connect(self.cos)
        self.ui.tan_btn.clicked.connect(self.tan)
        self.ui.cot_btn.clicked.connect(self.cot)
        self.ui.prcnt_btn.clicked.connect(self.percent)
        self.ui.pm_btn.clicked.connect(self.plmi)
        self.ui.dot_btn.clicked.connect(self.dot)
        self.ui.onex_btn.clicked.connect(self.rev)
        self.ui.fa_btn.clicked.connect(self.fact)
        self.ui.log_btn.clicked.connect(self.log)
        self.ui.sqrt_btn.clicked.connect(self.sqrt)

    def sqrt(self):

        self.num1 = int(self.ui.textbox.text())
        self.num1 = math.sqrt(self.num1)
        self.ui.textbox.setText(str(self.num1))


    def log(self):
        self.num1 = math.log(int(self.ui.textbox.text()))
        self.ui.textbox.setText(str(self.num1))

    def fact(self):
        self.num1 = math.factorial(int(self.ui.textbox.text()))
        self.ui.textbox.setText(str(self.num1))

    def rev(self):
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText(str(float(1 / self.num1)))

    def sum(self):
            self.num1 = float(self.ui.textbox.text())
            self.ui.textbox.setText('')
            self.flag_sum = True
   

    def sub(self):
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText('')
        self.flag_sub = True

    def div(self):
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText('')
        self.flag_div = True

    def mul(self):
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText('')
        self.flag_mul = True

    def sin(self):
        a = math.radians(float(self.ui.textbox.text()))
        self.ui.textbox.setText(str(math.sin(a)))

    def cos(self):
        a = math.radians(float(self.ui.textbox.text()))
        self.ui.textbox.setText(str(math.cos(a)))

    def tan(self):
        a = math.radians(float(self.ui.textbox.text()))
        self.ui.textbox.setText(str(math.tan(a)))

    def cot(self):
        a = math.radians(float(self.ui.textbox.text()))
        self.ui.textbox.setText(str(math.cot(a)))


    def percent(self):
        self.num1 = float(self.ui.textbox.text())
        self.num1 /= 100
        self.ui.textbox.setText(str(self.num1))

    def dot(self):
        for word in self.ui.textbox.text():
            if word == '.':
                break
            else:
                self.ui.textbox.setText(self.ui.textbox.text() + '.')

    def equal(self):
        self.num2 = float(self.ui.textbox.text())

        
        if self.flag_sum:
            result = self.num1 + self.num2
            self.ui.textbox.setText(str(result))

        elif self.flag_sub:
            result = self.num1 - self.num2
            self.ui.textbox.setText(str(result))

        elif self.flag_div:
            result = self.num1 // self.num2
            self.ui.textbox.setText(str(result))

        elif self.flag_mul:
            result = self.num1 * self.num2
            self.ui.textbox.setText(str(result))

    def plmi(self):
            self.num1 = float(self.ui.textbox.text())
            self.num1 *= -1
            self.ui.textbox.setText(str(self.num1))


    def clear(self):
        self.ui.textbox.setText('')


    def btn_numbers(self, i):
        if self.ui.textbox.text() == '' or self.ui.textbox.text() == '0' :
            self.ui.textbox.setText(str(i))
        else:
            self.ui.textbox.setText(str(self.ui.textbox.text()) + str(i))



app = QApplication([''])
window = Calculator()

app.exec()