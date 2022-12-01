# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'freeenzTXOV.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import PySide6
import PySide6.QtGui
from PySide6.QtWidgets import QApplication,QLabel,QDateEdit, QLabel, QLineEdit,QPushButton, QStatusBar,QWidget
import os
import sys


# PySide6のアプリ本体（ユーザがコーディングしていく部分）
class MainWindow(QWidget):
    def __init__(self, parent=None):
        # 親クラスの初期化
        super().__init__(parent)
        
        # ウィンドウタイトル
        self.setWindowTitle("PySide6で作ったアプリです。")
        windowWidth = 1000  # ウィンドウの横幅
        windowHeight = 800  # ウィンドウの高さ
        
        # ウィンドウサイズの変更
        self.resize(windowWidth, windowHeight)
        self.setFixedSize(windowWidth, windowHeight)
        self.SetLabel()        
    def SetLabel(self):
        label = QLabel(self)
        labelStyle ="QLabel {font-size: 30px}"
        label.setStyleSheet(labelStyle)
        label.setText("フリー加速計算")   

        labelStyle1 ="QLabel {font-size: 25px}"

        label1 = QLabel(self)
        label1.setStyleSheet(labelStyle1)
        label1.setText("1分加速")   
        label1.move(100, 120)
        
        label2 = QLabel(self)
        label2.setText("5分加速")   
        label2.setStyleSheet(labelStyle1)
        label2.move(140, 120)

        label3 = QLabel(self)
        label3.setStyleSheet(labelStyle1)
        label3.setText("10分加速")   
        label3.move(180, 120)

        label4 = QLabel(self)
        label4.setStyleSheet(labelStyle1)
        label4.setText("15分加速")   
        label4.move(220, 120)

        label5 = QLabel(self)
        label5.setStyleSheet(labelStyle1)
        label5.setText("30分加速")   
        label5.move(260, 120)

        label6 = QLabel(self)
        label6.setStyleSheet(labelStyle1)
        label6.setText("60分加速")   
        label6.move(300, 120)

        label7 = QLabel(self)
        label7.setStyleSheet(labelStyle1)
        label7.setText("3時間加速")   
        label7.move(340, 120)

        label8 = QLabel(self)
        label8.setStyleSheet(labelStyle1)
        label8.setText("8時間加速")   
        label8.move(380, 120)

        label9 = QLabel(self)
        label9.setStyleSheet(labelStyle1)
        label9.setText("15時間加速")   
        label9.move(420, 120)

        label10 = QLabel(self)
        label10.setStyleSheet(labelStyle1)
        label10.setText("24時間加速")   
        label10.move(460, 120)

        label11 = QLabel(self)
        label11.setStyleSheet(labelStyle1)
        label11.setText("3日加速")   
        label11.move(500, 120)       


if __name__ == "__main__":
    # 環境変数にPySide6を登録
    dirname = os.path.dirname(PySide6.__file__)
    plugin_path = os.path.join(dirname, 'plugins', 'platforms')
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
    
    app = QApplication(sys.argv)    # PySide6の実行
    window = MainWindow()           # ユーザがコーディングしたクラス
    window.show()                   # PySide6のウィンドウを表示
    sys.exit(app.exec()) 