import sys

from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication

'''
PyQt5 使用自定义信号和槽来关闭窗口(给窗口类添加信号)
'''


class WinSignalDemo(QWidget):
    button_clicked_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("使用自定义信号和槽来关闭窗口(给窗口类添加信号)")
        self.resize(300, 200)

        btn = QPushButton('关闭窗口', self)
        btn.clicked.connect(self.btn_clicked)
        self.button_clicked_signal.connect(self.btn_close)

    def btn_clicked(self):
        self.button_clicked_signal.emit()

    def btn_close(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = WinSignalDemo()
    win.show()
    sys.exit(app.exec_())