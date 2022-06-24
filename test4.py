import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


def on_pb_Package_clicked(self):
    mydlg = QDialog(self)
    mysub = subWin1(mydlg)
    mydlg.setWindowTitle(mysub.windowTitle())
    mysub.show()
    mydlg.setMaximumSize(0, 0)
    mydlg.exec()
    if mysub.value:
        print(mysub.value)
    print('结束了')


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(457, 351)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.text_Info = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text_Info.setObjectName("text_Info")
        self.gridLayout_2.addWidget(self.text_Info, 0, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.pb_Yes = QtWidgets.QPushButton(self.widget)
        self.pb_Yes.setObjectName("pb_Yes")
        self.gridLayout.addWidget(self.pb_Yes, 0, 0, 1, 1)
        self.pb_No = QtWidgets.QPushButton(self.widget)
        self.pb_No.setObjectName("pb_No")
        self.gridLayout.addWidget(self.pb_No, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.widget, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "信息确认"))
        self.pb_Yes.setText(_translate("MainWindow", "Yes"))
        self.pb_No.setText(_translate("MainWindow", "No"))


class MyMainWin(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.setupUi(self)  # 加载窗体
        self.setWindowTitle('子窗口')
        self.pb_Yes.setText('确定')
        self.pb_No.setText('取消')

        self.value = ''
        self.myParent = parent
        self.closeall = 1

    @pyqtSlot()
    def on_pb_Yes_clicked(self):
        self.value = self.text_Info.toPlainText()
        self.close()

    @pyqtSlot()
    def on_pb_No_clicked(self):
        self.value = ''
        self.close()

    # 改写close函数，配合QDialog可实现阻塞效果
    def closeEvent(self, e):
        if self.closeall:
            try:
                self.myParent.close()
            except:
                pass


#########################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWin()
    myWin.show()
    sys.exit(app.exec_())
