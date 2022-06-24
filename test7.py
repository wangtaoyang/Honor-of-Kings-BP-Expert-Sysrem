import sys

from PyQt5 import sip
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QGridLayout, QPushButton


class MainUi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        '''
        初始化整体布局
        '''
        self.resize(1000, 800)
        self.desktopWidth = QApplication.desktop().width()  # 获取当前桌面的宽
        self.desktopHeight = QApplication.desktop().height()  # 获取当前桌面的高

        self.main_widget = QWidget()  # 创建窗口主部件
        self.main_widget.setObjectName('main_widget')  # 对象命名
        self.main_layout = QGridLayout()  # 创建网格布局的对象
        self.main_widget.setLayout(self.main_layout)  # 将主部件设置为网格布局

        self.init_left()  # 初始化左侧空间
        self.init_right()  # 初始化右侧空间

        # 将初始化完成的左侧、右侧空间加入整体空间的网格布局
        self.main_layout.addWidget(self.left_widget, 0, 0, 1, 1)
        self.main_layout.addWidget(self.right_widget1, 0, 1, 1, 6)
        # self.main_layout.addWidget(self.right_widget2, 0, 1, 1, 6)
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件

    def init_left(self):
        '''
        初始化左侧布局
        '''
        self.left_widget = QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')  # 左侧部件对象命名
        self.left_layout = QGridLayout()  # 创建网格布局对象
        self.left_widget.setLayout(self.left_layout)  # 将左侧部件设置为网格布局

    # 接下来添加按钮控件等...，细节略

    def init_right(self):
        '''
        初始化右侧布局
        '''
        self.right_widget1 = QWidget()  # 创建右侧界面1
        self.right_layout1 = QGridLayout()  # 创建网格布局对象1
        self.right_widget1.setLayout(self.right_layout1)  # 设置右侧界面1的布局为网格布局
        self.Button1 = QPushButton()  # 加一个用来界面跳转的button1
        self.Button1.setText("进入界面2")
        self.right_layout1.addWidget(self.Button1)

        self.right_widget2 = QWidget()  # 创建右侧界面2
        self.right_layout2 = QGridLayout()  # 创建网格布局对象2
        self.right_widget2.setLayout(self.right_layout2)  # 设置右侧界面2的布局为网格布局
        self.Button2 = QPushButton()  # 加一个用来界面跳转的button2
        self.Button2.setText("进入界面1")
        self.right_layout2.addWidget(self.Button2)

        # 把切换界面的button和两个跳转函数绑定
        self.Button1.clicked.connect(self.clicked_1)
        self.Button2.clicked.connect(self.clicked_2)

    # import sip
    def clicked_1(self):
        # 删除界面1
        self.main_layout.removeWidget(self.right_widget1)
        sip.delete(self.right_widget1)
        # 创建界面2
        self.right_widget2 = QWidget()  # 创建右侧界面2
        self.right_layout2 = QGridLayout()  # 创建网格布局对象2
        self.right_widget2.setLayout(self.right_layout2)  # 设置右侧界面2的布局为网格布局
        self.Button2 = QPushButton()  # 加一个用来界面跳转的button2
        self.Button2.setText("进入界面1")
        self.right_layout2.addWidget(self.Button2)
        # 添加界面2到总布局里
        self.main_layout.addWidget(self.right_widget2, 0, 1, 1, 6)

    def clicked_2(self):
        # 删除界面2
        self.main_layout.removeWidget(self.right_widget2)
        sip.delete(self.right_widget2)
        # 创建界面1
        self.right_widget1 = QWidget()  # 创建右侧界面1
        self.right_layout1 = QGridLayout()  # 创建网格布局对象1
        self.right_widget1.setLayout(self.right_layout1)  # 设置右侧界面2的布局为网格布局
        self.Button1 = QPushButton()  # 加一个用来界面跳转的button1
        self.Button1.setText("进入界面2")
        self.right_layout1.addWidget(self.Button1)
        # 添加界面1到总布局里
        self.main_layout.addWidget(self.right_widget1, 0, 1, 1, 6)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainUi()
    ui.show()
    sys.exit(app.exec_())
