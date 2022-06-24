from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import pyqtSignal
import sys
from t4 import t4
class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()
        self.initUI()

    def initUI(self):
        self.button = QPushButton('open', self)

        self.button.clicked.connect(self.new)

        self.setWindowTitle('Window')
        self.resize(200,200)

    def new(self):
        my = t4(self)
        # 在主窗口中连接信号和槽
        my.mySignal.connect(self.setText)
        my.exec_()

    # 实现槽函数
    def setText(self, connect):
        self.button.setText(connect)

if __name__ == "__main__":
        app = QApplication(sys.argv)
        w = Window()
        w.show()
        print('父类窗口大小'+str(w.pos()))
        sys.exit(app.exec_())

