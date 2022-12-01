
import sys,time
from PyQt6.QtWidgets import QApplication,QWidget,QDateTimeEdit,QVBoxLayout
from PyQt6.QtCore import QLocale,QDateTime
today_in = time.today()


class Madoka(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('font-family: Kaiti SC; font-size: 20px')
        vbl = QVBoxLayout()
        self.setLayout(vbl)
        hizuke = QDateTimeEdit(self)
        vbl.addWidget(hizuke)
        hizuke.setDateTime(QDateTime(2021,8,9,19,30)) # 初期値の時間
        hizuke.setCalendarPopup(True) # 暦を表示する
        koyomi = hizuke.calendarWidget()
        koyomi.setLocale(QLocale('jp')) # 暦のlocaleを変えてロシア語にしてみる

qAp = QApplication(sys.argv)
mado = Madoka()
mado.show()
qAp.exec()