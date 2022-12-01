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
        label.move(50, 100)
        label1 = QLabel(self)
        labelStyle1 ="QLabel {font-size: 20px}"
        label1.setStyleSheet(labelStyle1)
        label1.setText("1分加速")   
        label1.move(80, 120)
               


if __name__ == "__main__":
    # 環境変数にPySide6を登録
    dirname = os.path.dirname(PySide6.__file__)
    plugin_path = os.path.join(dirname, 'plugins', 'platforms')
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
    
    app = QApplication(sys.argv)    # PySide6の実行
    window = MainWindow()           # ユーザがコーディングしたクラス
    window.show()                   # PySide6のウィンドウを表示
    sys.exit(app.exec()) 