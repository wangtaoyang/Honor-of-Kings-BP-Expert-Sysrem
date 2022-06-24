from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import pyqtSignal
import sys
"""
自定义对话框
"""


class t4(QDialog):
    # 自定义信号
    mySignal = pyqtSignal(str)

    def __init__(self, parent=None):
        super(t4, self).__init__(parent)
        self.initUI()

    def initUI(self):

        button = QPushButton('发送', self)
        button.move(10, 40)

        button.clicked.connect(self.sendText)

        self.setWindowTitle('MyDialog')
        self.setGeometry(300, 300, 300, 200)

    def sendText(self):
        self.mySignal.emit('test2')  # 发射信号

if __name__ == "__main__":
        app = QApplication(sys.argv)
        w = t4()
        w.show()
        print('父类窗口大小'+str(w.pos()))
        sys.exit(app.exec_())
