

################################################################################
## WARNING! All changes made in this file will be lost when recompiling UI file!
##Created for game acceleration calculations
##Required to install the PySide6 library
##Japanese notation
##All values must be numbers
##If there is no value to enter, enter 0.
##If there are no values entered, an error will occur and the calculation will
##not be performed.
################################################################################

from cgi import print_arguments
import PySide6
import PySide6.QtGui
from PySide6.QtWidgets import QApplication,QLabel,QDateEdit, QLabel, QLineEdit,QPushButton, QStatusBar,QWidget,QDialog
import os
import sys
import datetime
from discordwebhook import Discord
import requests

class MainWindow(QWidget):
    def __init__(self, parent=None):
        # 親クラスの初期化
        super().__init__(parent)
        
        # ウィンドウタイトル
        self.setWindowTitle("フリー加速計算")
        windowWidth = 500  # ウィンドウの横幅
        windowHeight = 600  # ウィンドウの高さ
        
        # ウィンドウサイズの変更
        self.resize(windowWidth, windowHeight)
        self.setFixedSize(windowWidth, windowHeight)
        self.SetLabel() 
        self.SetLineedit()
        self.SetButton()

    def SetLabel(self):
        label = QLabel(self)
        labelStyle ="QLabel {font-size: 30px}"
        label.setStyleSheet(labelStyle)
        label.setText("フリー加速計算")   

        labelStyle1 ="QLabel {font-size: 25px}"



        label1 = QLabel(self)
        label1.setStyleSheet(labelStyle1)
        label1.setText("1分加速")   
        label1.move(80, 100)

 
        
        label2 = QLabel(self)
        label2.setText("5分加速")   
        label2.setStyleSheet(labelStyle1)
        label2.move(80, 140)

        label3 = QLabel(self)
        label3.setStyleSheet(labelStyle1)
        label3.setText("10分加速")   
        label3.move(80, 180)

        label4 = QLabel(self)
        label4.setStyleSheet(labelStyle1)
        label4.setText("15分加速")   
        label4.move(80, 220)

        label5 = QLabel(self)
        label5.setStyleSheet(labelStyle1)
        label5.setText("30分加速")   
        label5.move(80, 260)

        label6 = QLabel(self)
        label6.setStyleSheet(labelStyle1)
        label6.setText("60分加速")   
        label6.move(80, 300)

        label7 = QLabel(self)
        label7.setStyleSheet(labelStyle1)
        label7.setText("3時間加速")   
        label7.move(80, 340)

        label8 = QLabel(self)
        label8.setStyleSheet(labelStyle1)
        label8.setText("8時間加速")   
        label8.move(80, 380)

        label9 = QLabel(self)
        label9.setStyleSheet(labelStyle1)
        label9.setText("15時間加速")   
        label9.move(80, 420)

        label10 = QLabel(self)
        label10.setStyleSheet(labelStyle1)
        label10.setText("24時間加速")   
        label10.move(80, 460)

        label11 = QLabel(self)
        label11.setStyleSheet(labelStyle1)
        label11.setText("3日加速")   
        label11.move(80, 500)    
        
        

#テキストボックス
    def SetLineedit(self):
        self.free_1m = QLineEdit(self) 
        self.free_1m.move(250, 105) 
        self.free_1m.resize(150, 25)  
        
        
        
        self.free_5m = QLineEdit(self) 
        self.free_5m.move(250, 145) 
        self.free_5m.resize(150, 25)  

        self.free_10m = QLineEdit(self) 
        self.free_10m.move(250, 185) 
        self.free_10m.resize(150, 25)  
        
        self.free_15m = QLineEdit(self) 
        self.free_15m.move(250, 225) 
        self.free_15m.resize(150, 25)  
        
        self.free_30m = QLineEdit(self) 
        self.free_30m.move(250, 265) 
        self.free_30m.resize(150, 25)  
        
        self.free_60m = QLineEdit(self) 
        self.free_60m.move(250, 305) 
        self.free_60m.resize(150, 25)  
        
        self.free_3h = QLineEdit(self) 
        self.free_3h.move(250, 345) 
        self.free_3h.resize(150, 25)  
        
        self.free_8h = QLineEdit(self) 
        self.free_8h.move(250, 385) 
        self.free_8h.resize(150, 25)  

        self.free_15h = QLineEdit(self) 
        self.free_15h.move(250, 425) 
        self.free_15h.resize(150, 25)  

        self.free_24h = QLineEdit(self) 
        self.free_24h.move(250, 465) 
        self.free_24h.resize(150, 25)  

        self.free_72h = QLineEdit(self) 
        self.free_72h.move(250, 505) 
        self.free_72h.resize(150, 25)  

#プッシュボタン
    def SetButton(self):
        button_sent = QPushButton(self)
        button_sent.setText("実行")
        button_sent.move(400, 550) 
        button_sent.pressed.connect(self.CallbackButtonPressed)
        
    def CallbackButtonPressed(self):
        Fre_01ms = int(self.free_1m.text())*1*1
        Fre_05ms = int(self.free_5m.text())*5*1
        Fre_10ms = int(self.free_10m.text())*10*1
        Fre_15ms = int(self.free_15m.text())*15*1
        Fre_30ms = int(self.free_30m.text())*30*1
        Fre_60ms = int(self.free_60m.text())*60*1
        Fre_03hs = int(self.free_3h.text())*60*3
        Fre_08hs = int(self.free_8h.text())*60*8
        Fre_15hs = int(self.free_15h.text())*60*15
        Fre_24hs = int(self.free_24h.text())*60*24
        Fre_72hs = int(self.free_72h.text())*60*72
        Fre_total  = Fre_01ms  + Fre_05ms + Fre_10ms + Fre_15ms + Fre_30ms + Fre_60ms + Fre_03hs + Fre_08hs + Fre_15hs + Fre_24hs + Fre_72hs
        print(Fre_total)
        free_to_hour = Fre_total//60
        free_to_days = Fre_total//(24*60)
        print(str(free_to_hour) + '時間分')
        print(str(free_to_days) +'日分の加速です')
        global input_day
        input_day = datetime.date.today()

        input_day_02 = input_day.strftime('%Y年%m月%d日')

        Fre_01ms_str = str('{:8,d}'.format(Fre_01ms))
        Fre_05ms_str = str('{:8,d}'.format(Fre_05ms))
        Fre_10ms_str = str('{:8,d}'.format(Fre_10ms))
        Fre_15ms_str = str('{:8,d}'.format(Fre_15ms))
        Fre_30ms_str = str('{:8,d}'.format(Fre_30ms))
        Fre_60ms_str = str('{:8,d}'.format(Fre_60ms))
        Fre_03hs_str = str('{:8,d}'.format(Fre_03hs))
        Fre_08hs_str = str('{:8,d}'.format(Fre_08hs))
        Fre_15hs_str = str('{:8,d}'.format(Fre_15hs))
        Fre_24hs_str = str('{:8,d}'.format(Fre_24hs))
        Fre_72hs_str = str('{:8,d}'.format(Fre_72hs))
        Fre_total_str = str('{:8,d}'.format(Fre_total))
        free_to_hour_str = str('{:8,d}'.format(free_to_hour))
        free_to_days_str = str('{:8,d}'.format(free_to_days))



        print(input_day_02+'日現在のフリー加速の数量は'+'\n'+'1分加速：'+Fre_01ms_str+'\n'+'5分加速：'+Fre_05ms_str+'\n'+'10分加速：'+Fre_10ms_str+'\n'+'15分加速：'+Fre_15ms_str+'\n'+'30分加速：'+Fre_30ms_str+'\n'+'60分加速：'+Fre_60ms_str+'\n'+'3時間加速：'+Fre_03hs_str+'\n'+'8時間加速：'+Fre_08hs_str+'\n'+'15時間加速：'+Fre_15hs_str+'\n'+'24時間加速：'+Fre_24hs_str+'\n'+'3日加速：'+Fre_72hs_str+'\n'+'合計（分)：'+Fre_total_str+'分\n\n'+'合計（時)：'+free_to_hour_str+'時間\n'+'合計（日)：'+free_to_days_str+'日分の加速があります')
        '''
        discord = Discord(url="")
        discord.post(content=sentmag_01)
        #lineへメッセージを送る
        url = "https://notify-api.line.me/api/notify"
        access_token = ''
        headers = {'Authorization': 'Bearer ' + access_token}

        message = content=sentmag_01
        payload = {'message': message}
        r = requests.post(url, headers=headers, params=payload,)
        '''        
        
        
        dialog = QDialog()                              # ダイアログを使うことを宣言
        dialog.setWindowTitle("計算の結果です") # ダイアログのタイトル
        
        label2 = QLabel(dialog)                  # 「ダイアログで」ラベルを使うことを宣言
        label2.setText(str(free_to_days) +'日分の加速です')     # ラベルに文字を設定
        label2.setStyleSheet("font-size: 24px;") # ラベル文字の大きさ
        
        # ダイアログをラベルの大きさに合わせる
        labelWidth = label2.sizeHint().width()   # ラベルの横幅
        labelHeight = label2.sizeHint().height() # ラベルの高さ
        dialog.resize(labelWidth, labelHeight)  # ダイアログのサイズ変更
        
        # ダイアログを表示
        dialog.exec()
        
        
        a1s = datetime.date.today()
        input_day = a1s.strftime('%Y年%m月%d日')

        
        


        
if __name__ == "__main__":
    # 環境変数にPySide6を登録
    dirname = os.path.dirname(PySide6.__file__)
    plugin_path = os.path.join(dirname, 'plugins', 'platforms')
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
    
    app = QApplication(sys.argv)    # PySide6の実行
    window = MainWindow()           # ユーザがコーディングしたクラス
    window.show()                   # PySide6のウィンドウを表示
    sys.exit(app.exec()) 