import sys
from PyQt5.QtWidgets import QApplication, QWidget
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(300,100)
    w.setWindowTitle("ใในใ")
    w.show()
    sys.exit(app.exec_())