import time

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
import sys


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("主窗口")
        button = QPushButton("弹出子窗", self)
        button.clicked.connect(self.show_child)

    def show_child(self):
        child_window = Child()
        child_window.show()
        time.sleep(4)
        child_window.close()


class Child(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("我是子窗口啊")
        # quit = QPushButton("Close", self)
        # quit.setGeometry(10, 10, 100, 60)
        # quit.setStyleSheet("background-color: red")  # 设置按钮的风格和颜色
        # quit.clicked.connect(self.close)  # 点击按钮之后关闭窗口
        #
        # self.timer = QTimer(self)  # 初始化一个定时器
        # self.timer.timeout.connect(self.close)  # 计时结束调用operate()方法
        # self.timer.start(2000)  # 设置计时间隔并启动 2s后关闭窗口


# 运行主窗口
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Main()
    window.show()

    sys.exit(app.exec_())
