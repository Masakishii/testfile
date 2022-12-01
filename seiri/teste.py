from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication([])  # アプリケーションを作成
ui_path = "ui_files"
dlg1 = uic.loadUi(f"{ui_path}/freee.ui")  # 作成した page1.ui を読み出して, ダイアログ1を作成

if __name__ == "__main__":
    QtWidgets.show()  # ダイアログ1を表示
    app.exec()   # 実行