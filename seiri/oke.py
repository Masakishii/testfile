# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'oke.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(623, 451)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 340, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 340, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(390, 10, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dateEdit.setFont(font)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 12, 31), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setObjectName("dateEdit")
        self.free1 = QtWidgets.QLineEdit(self.centralwidget)
        self.free1.setGeometry(QtCore.QRect(140, 80, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.free1.setFont(font)
        self.free1.setText("")
        self.free1.setObjectName("free1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 80, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 120, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.free5 = QtWidgets.QLineEdit(self.centralwidget)
        self.free5.setGeometry(QtCore.QRect(140, 120, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.free5.setFont(font)
        self.free5.setText("")
        self.free5.setObjectName("free5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 200, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.free15 = QtWidgets.QLineEdit(self.centralwidget)
        self.free15.setGeometry(QtCore.QRect(140, 200, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.free15.setFont(font)
        self.free15.setText("")
        self.free15.setObjectName("free15")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 160, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.free10 = QtWidgets.QLineEdit(self.centralwidget)
        self.free10.setGeometry(QtCore.QRect(140, 160, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.free10.setFont(font)
        self.free10.setText("")
        self.free10.setObjectName("free10")
        self.free60 = QtWidgets.QLineEdit(self.centralwidget)
        self.free60.setGeometry(QtCore.QRect(140, 280, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.free60.setFont(font)
        self.free60.setText("")
        self.free60.setObjectName("free60")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 240, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.free30 = QtWidgets.QLineEdit(self.centralwidget)
        self.free30.setGeometry(QtCore.QRect(140, 240, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.free30.setFont(font)
        self.free30.setText("")
        self.free30.setObjectName("free30")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(40, 280, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(360, 120, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(350, 200, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.free8h = QtWidgets.QLineEdit(self.centralwidget)
        self.free8h.setGeometry(QtCore.QRect(470, 120, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.free8h.setFont(font)
        self.free8h.setText("")
        self.free8h.setObjectName("free8h")
        self.free15h = QtWidgets.QLineEdit(self.centralwidget)
        self.free15h.setGeometry(QtCore.QRect(470, 160, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.free15h.setFont(font)
        self.free15h.setText("")
        self.free15h.setObjectName("free15h")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(380, 240, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.free24h = QtWidgets.QLineEdit(self.centralwidget)
        self.free24h.setGeometry(QtCore.QRect(470, 200, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.free24h.setFont(font)
        self.free24h.setText("")
        self.free24h.setObjectName("free24h")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(360, 80, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.free3d = QtWidgets.QLineEdit(self.centralwidget)
        self.free3d.setGeometry(QtCore.QRect(470, 240, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.free3d.setFont(font)
        self.free3d.setText("")
        self.free3d.setObjectName("free3d")
        self.free3h = QtWidgets.QLineEdit(self.centralwidget)
        self.free3h.setGeometry(QtCore.QRect(470, 80, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.free3h.setFont(font)
        self.free3h.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.free3h.setText("")
        self.free3h.setObjectName("free3h")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(350, 160, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.free1, self.free5)
        MainWindow.setTabOrder(self.free5, self.free10)
        MainWindow.setTabOrder(self.free10, self.free15)
        MainWindow.setTabOrder(self.free15, self.free30)
        MainWindow.setTabOrder(self.free30, self.free60)
        MainWindow.setTabOrder(self.free60, self.free3h)
        MainWindow.setTabOrder(self.free3h, self.free8h)
        MainWindow.setTabOrder(self.free8h, self.free15h)
        MainWindow.setTabOrder(self.free15h, self.free24h)
        MainWindow.setTabOrder(self.free24h, self.free3d)
        MainWindow.setTabOrder(self.free3d, self.dateEdit)
        MainWindow.setTabOrder(self.dateEdit, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.pushButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "?????????"))
        self.pushButton_2.setText(_translate("MainWindow", "??????"))
        self.dateEdit.setDisplayFormat(_translate("MainWindow", "yyyy???MM???dd???"))
        self.label.setText(_translate("MainWindow", "1?????????"))
        self.label_2.setText(_translate("MainWindow", "5?????????"))
        self.label_3.setText(_translate("MainWindow", "15?????????"))
        self.label_4.setText(_translate("MainWindow", "10?????????"))
        self.label_7.setText(_translate("MainWindow", "30?????????"))
        self.label_8.setText(_translate("MainWindow", "60?????????"))
        self.label_5.setText(_translate("MainWindow", "8????????????"))
        self.label_6.setText(_translate("MainWindow", "24????????????"))
        self.label_10.setText(_translate("MainWindow", "3?????????"))
        self.label_11.setText(_translate("MainWindow", "3????????????"))
        self.label_12.setText(_translate("MainWindow", "15????????????"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
