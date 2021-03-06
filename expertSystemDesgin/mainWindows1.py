# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindows.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys
import requests
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog
from subWindows import Ui_Form
import rules

class Ui_MainWindow(object):
    enemy = []
    my_team1 = {}
    my_team2 = {}
    my_team3 = {}

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(890, 658)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(90, 50, 100, 100))
        self.pushButton_1.setObjectName("pushButton_1")

        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(100, 160, 75, 23))
        self.label_1.setObjectName("label_1")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 50, 100, 100))
        self.pushButton_2.setObjectName("pushButton_2")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 160, 75, 23))
        self.label_2.setObjectName("label_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(390, 50, 100, 100))
        self.pushButton_3.setObjectName("pushButton_3")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(400, 160, 75, 23))
        self.label_3.setObjectName("label_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(540, 50, 100, 100))
        self.pushButton_4.setObjectName("pushButton_4")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(550, 160, 75, 23))
        self.label_4.setObjectName("label_4")

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(690, 50, 100, 100))
        self.pushButton_5.setObjectName("pushButton_5")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(700, 160, 75, 23))
        self.label_5.setObjectName("label_5")

        self.fix_label_6 = QtWidgets.QLabel(self.centralwidget)
        self.fix_label_6.setGeometry(QtCore.QRect(100, 390, 75, 23))
        self.fix_label_6.setObjectName("fix_label_6")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(90, 280, 100, 100))
        self.label_6.setObjectName("label_6")

        self.fix_label_7 = QtWidgets.QLabel(self.centralwidget)
        self.fix_label_7.setGeometry(QtCore.QRect(250, 390, 75, 23))
        self.fix_label_7.setObjectName("fix_label_7")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(240, 280, 100, 100))
        self.label_7.setObjectName("label_7")

        self.fix_label_8 = QtWidgets.QLabel(self.centralwidget)
        self.fix_label_8.setGeometry(QtCore.QRect(400, 390, 75, 23))
        self.fix_label_8.setObjectName("fix_label_8")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(390, 280, 100, 100))
        self.label_8.setObjectName("label_8")

        self.fix_label_9 = QtWidgets.QLabel(self.centralwidget)
        self.fix_label_9.setGeometry(QtCore.QRect(550, 390, 75, 23))
        self.fix_label_9.setObjectName("fix_label_9")

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(540, 280, 100, 100))
        self.label_9.setObjectName("label_9")

        self.fix_label_10 = QtWidgets.QLabel(self.centralwidget)
        self.fix_label_10.setGeometry(QtCore.QRect(700, 390, 75, 23))
        self.fix_label_10.setObjectName("fix_label_10")

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(690, 280, 100, 100))
        self.label_10.setObjectName("label_10")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(100, 480, 690, 120))
        self.textBrowser.setObjectName("textBrowser")

        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(250, 430, 75, 23))
        self.pushButton_11.setObjectName("pushButton_11")

        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(400, 430, 75, 23))
        self.pushButton_12.setObjectName("pushButton_12")

        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(550, 430, 75, 23))
        self.pushButton_13.setObjectName("pushButton_13")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_1.setText(_translate("MainWindow", "????????????1"))
        self.pushButton_1.clicked.connect(lambda: self.show_child(1, self.label_1.text()))

        self.label_2.setText(_translate("MainWindow", "????????????2"))
        self.pushButton_2.clicked.connect(lambda: self.show_child(2, self.label_2.text()))

        self.label_3.setText(_translate("MainWindow", "????????????3"))
        self.pushButton_3.clicked.connect(lambda: self.show_child(3, self.label_3.text()))

        self.label_4.setText(_translate("MainWindow", "????????????4"))
        self.pushButton_4.clicked.connect(lambda: self.show_child(4, self.label_4.text()))

        self.label_5.setText(_translate("MainWindow", "????????????5"))
        self.pushButton_5.clicked.connect(lambda: self.show_child(5, self.label_5.text()))

        self.fix_label_6.setText(_translate("MainWindow", "????????????1"))
        self.fix_label_7.setText(_translate("MainWindow", "????????????2"))
        self.fix_label_8.setText(_translate("MainWindow", "????????????3"))
        self.fix_label_9.setText(_translate("MainWindow", "????????????4"))
        self.fix_label_10.setText(_translate("MainWindow", "????????????5"))

        self.pushButton_11.setText(_translate("MainWindow", "????????????"))
        self.pushButton_11.clicked.connect(lambda : self.analyse_my_heroes())
        self.pushButton_12.setText(_translate("MainWindow", "???????????????"))
        self.pushButton_13.setText(_translate("MainWindow", "???????????????"))

        default_img_path = 'default_head.png'
        self.pushButton_1.setIcon(QtGui.QIcon(default_img_path))
        self.pushButton_1.setIconSize(QtCore.QSize(100, 100))

        self.pushButton_2.setIcon(QtGui.QIcon(default_img_path))
        self.pushButton_2.setIconSize(QtCore.QSize(100, 100))

        self.pushButton_3.setIcon(QtGui.QIcon(default_img_path))
        self.pushButton_3.setIconSize(QtCore.QSize(100, 100))

        self.pushButton_4.setIcon(QtGui.QIcon(default_img_path))
        self.pushButton_4.setIconSize(QtCore.QSize(100, 100))

        self.pushButton_5.setIcon(QtGui.QIcon(default_img_path))
        self.pushButton_5.setIconSize(QtCore.QSize(100, 100))

        self.label_6.setGeometry(QtCore.QRect(90, 280, 100, 100))
        self.label_6.setPixmap(QPixmap('default_head.png'))  # ????????????
        self.label_6.setScaledContents(True)  # ??????????????????label??????

        self.label_7.setGeometry(QtCore.QRect(240, 280, 100, 100))
        self.label_7.setPixmap(QPixmap('default_head.png'))  # ????????????
        self.label_7.setScaledContents(True)  # ??????????????????label??????

        self.label_8.setGeometry(QtCore.QRect(390, 280, 100, 100))
        self.label_8.setPixmap(QPixmap('default_head.png'))  # ????????????
        self.label_8.setScaledContents(True)  # ??????????????????label??????

        self.label_9.setGeometry(QtCore.QRect(540, 280, 100, 100))
        self.label_9.setPixmap(QPixmap('default_head.png'))  # ????????????
        self.label_9.setScaledContents(True)  # ??????????????????label??????

        self.label_10.setGeometry(QtCore.QRect(690, 280, 100, 100))
        self.label_10.setPixmap(QPixmap('default_head.png'))  # ????????????
        self.label_10.setScaledContents(True)  # ??????????????????label??????

    def show_child(self, index, to_replace_name):
        child_window = Ui_Form(index, to_replace_name)
        child_window.heroSignal.connect(self.showHero)
        Form = QDialog()
        child_window.setupUi(Form)
        Form.exec_()

        # app = QApplication(sys.argv)
        # Form = QDialog()
        # ui = Ui_Form(1)
        # ui.setupUi(Form)
        # Form.show()
        # sys.exit(app.exec_())

    def showHero(self, context: dict):
        _translate = QtCore.QCoreApplication.translate
        image_path = context['path']
        if context['name'] in self.enemy:
            return
        else:
            if context['to_replace_name'] in self.enemy:
                self.enemy.remove(context['to_replace_name'])
            self.enemy.append(context['name'])

        if context['index'] == 1:
            self.pushButton_1.setIcon(QtGui.QIcon(image_path))
            self.pushButton_1.setIconSize(QtCore.QSize(100, 100))
            self.label_1.setText(_translate("MainWindow", context['name']))
            self.label_1.setAlignment(Qt.AlignCenter)
        elif context['index'] == 2:
            self.pushButton_2.setIcon(QtGui.QIcon(image_path))
            self.pushButton_2.setIconSize(QtCore.QSize(100, 100))
            self.label_2.setText(_translate("MainWindow", context['name']))
            self.label_2.setAlignment(Qt.AlignCenter)
        elif context['index'] == 3:
            self.pushButton_3.setIcon(QtGui.QIcon(image_path))
            self.pushButton_3.setIconSize(QtCore.QSize(100, 100))
            self.label_3.setText(_translate("MainWindow", context['name']))
            self.label_3.setAlignment(Qt.AlignCenter)
        elif context['index'] == 4:
            self.pushButton_4.setIcon(QtGui.QIcon(image_path))
            self.pushButton_4.setIconSize(QtCore.QSize(100, 100))
            self.label_4.setText(_translate("MainWindow", context['name']))
            self.label_4.setAlignment(Qt.AlignCenter)
        elif context['index'] == 5:
            self.pushButton_5.setIcon(QtGui.QIcon(image_path))
            self.pushButton_5.setIconSize(QtCore.QSize(100, 100))
            self.label_5.setText(_translate("MainWindow", context['name']))
            self.label_5.setAlignment(Qt.AlignCenter)

    def analyse_my_heroes(self):
        _translate = QtCore.QCoreApplication.translate
        info = rules.compare_all_enemy(self.enemy)
        reason = ''

        path = "touxiang/{0}.jpg".format(info[0]['name'])
        self.label_6.setGeometry(QtCore.QRect(90, 280, 100, 100))
        self.label_6.setPixmap(QPixmap(path))  # ????????????
        self.label_6.setScaledContents(True)  # ??????????????????label??????
        self.fix_label_6.setText(_translate("MainWindow", info[0]['name']))
        self.fix_label_6.setAlignment(Qt.AlignCenter)

        path = "touxiang/{0}.jpg".format(info[1]['name'])
        self.label_7.setGeometry(QtCore.QRect(240, 280, 100, 100))
        self.label_7.setPixmap(QPixmap(path))  # ????????????
        self.label_7.setScaledContents(True)  # ??????????????????label??????
        self.fix_label_7.setText(_translate("MainWindow", info[1]['name']))
        self.fix_label_7.setAlignment(Qt.AlignCenter)

        path = "touxiang/{0}.jpg".format(info[2]['name'])
        self.label_8.setGeometry(QtCore.QRect(390, 280, 100, 100))
        self.label_8.setPixmap(QPixmap(path))  # ????????????
        self.label_8.setScaledContents(True)  # ??????????????????label??????
        self.fix_label_8.setText(_translate("MainWindow", info[2]['name']))
        self.fix_label_8.setAlignment(Qt.AlignCenter)

        path = "touxiang/{0}.jpg".format(info[3]['name'])
        self.label_9.setGeometry(QtCore.QRect(540, 280, 100, 100))
        self.label_9.setPixmap(QPixmap(path))  # ????????????
        self.label_9.setScaledContents(True)  # ??????????????????label??????
        self.fix_label_9.setText(_translate("MainWindow", info[3]['name']))
        self.fix_label_9.setAlignment(Qt.AlignCenter)

        path = "touxiang/{0}.jpg".format(info[4]['name'])
        self.label_10.setGeometry(QtCore.QRect(690, 280, 100, 100))
        self.label_10.setPixmap(QPixmap(path))  # ????????????
        self.label_10.setScaledContents(True)  # ??????????????????label??????
        self.fix_label_10.setText(_translate("MainWindow", info[4]['name']))
        self.fix_label_10.setAlignment(Qt.AlignCenter)

        for hero in info:
            reason += "\n".join(hero['reason'])

        self.textBrowser.setText(reason)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Ui_MainWindow()
    MainWindow = QtWidgets.QMainWindow()

    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
