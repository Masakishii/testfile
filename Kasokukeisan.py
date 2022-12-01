

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
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

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
        self.free_01m = QLineEdit(self) 
        self.free_01m.move(250, 105) 
        self.free_01m.resize(150, 25)  
        
        
        
        self.free_05m = QLineEdit(self) 
        self.free_05m.move(250, 145) 
        self.free_05m.resize(150, 25)  

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
        
        self.free_03h = QLineEdit(self) 
        self.free_03h.move(250, 345) 
        self.free_03h.resize(150, 25)  
        
        self.free_08h = QLineEdit(self) 
        self.free_08h.move(250, 385) 
        self.free_08h.resize(150, 25)  

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
        
        free_01m_a = int(self.free_01m.text())
        free_05m_a = int(self.free_05m.text())
        free_10m_a = int(self.free_10m.text())
        free_15m_a = int(self.free_15m.text())
        free_30m_a = int(self.free_30m.text())
        free_60m_a = int(self.free_60m.text())
        free_03h_a = int(self.free_03h.text())
        free_08h_a = int(self.free_08h.text())
        free_15h_a = int(self.free_15h.text())
        free_24h_a = int(self.free_24h.text())
        free_72h_a = int(self.free_72h.text())
        
        
        
        Fre_01ms = free_01m_a*1*1
        Fre_05ms = free_05m_a*5*1
        Fre_10ms = free_10m_a*10*1
        Fre_15ms = free_15m_a*15*1
        Fre_30ms = free_30m_a*30*1
        Fre_60ms = free_60m_a*60*1
        Fre_03hs = free_03h_a*60*3
        Fre_08hs = free_08h_a*60*8
        Fre_15hs = free_15h_a*60*15
        Fre_24hs = free_24h_a*60*24
        Fre_72hs = free_72h_a*60*72
        
        Fre_total  = Fre_01ms  + Fre_05ms + Fre_10ms + Fre_15ms + Fre_30ms + Fre_60ms + Fre_03hs + Fre_08hs + Fre_15hs + Fre_24hs + Fre_72hs
        print(Fre_total)
        free_to_hour = Fre_total//60
        free_to_days = Fre_total//(24*60)
        print(str(free_to_hour) + '時間分')
        print(str(free_to_days) +'日分の加速です')
        global input_day
        input_day = datetime.date.today()
#Google spreadsheetに転記するための準備リスト

        input_day_02 = input_day.strftime('%Y年%m月%d日')
'''
        inputlist_00 = ['加速数量',input_day_02,free_01m_a,free_05m_a,free_10m_a,free_15m_a,free_30m_a,free_60m_a,free_03h_a,free_08h_a,free_15h_a,free_24h_a,free_72h_a]
        inputlist_01 = ['加速分換算',input_day_02,Fre_01ms,Fre_05ms,Fre_10ms,Fre_15ms,Fre_30ms,Fre_60ms,Fre_03hs,Fre_08hs,Fre_15hs,Fre_24hs,Fre_72hs]
        inputlist_02 = ['加速合計',input_day_02,Fre_total,free_to_hour,free_to_days]
        inputlist_03 = [inputlist_00,inputlist_01,inputlist_02]
        print(inputlist_03)
'''

        
#Google spreadsheetに転記
'''
        print(inputlist_03)
        #見ずらいから表示方法変更
        df = pd.DataFrame(inputlist_03)
        print(df)
        #リストの数はいくつ？
        list_index_num = df.shape[0]
        list_cloum_num = df.shape[1]

        #これが繰り返す数　列：行
        print(str(list_cloum_num) + ':' + str(list_index_num))

        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

        #googleスプレッドシートの処理
        #ダウンロードしたjsonファイルをドライブにアップデートした際のパス
        json ='/client_secret.json'

        credentials = ServiceAccountCredentials.from_json_keyfile_name(json, scope)

        gc = gspread.authorize(credentials)

        #書き込み先のスプレッドシートキーを追加
        SPREADSHEET_KEY = ''

        #これから下のコードが繰り返し処理
        i = 0       #行数処理用
        q = 0       #列数処理用


        input_data = inputlist_03

        while i < list_index_num:
            Sheet_Name_01 = input_data[i][q]


            WS_01 = gc.open_by_key(SPREADSHEET_KEY).worksheet(Sheet_Name_01)
            def next_available_row(WS_01):
                str_list = list(filter(None, WS_01.col_values(1)))
                return str(len(str_list)+1)
            next_row = next_available_row(WS_01)
            chars = list(filter(None, input_data[i]))
            list_b = list(filter(None, chars))
            list_cloum_num = len(list_b)

            q = q + 1
            while q < list_cloum_num:
                    Value_Get_01 = input_data[i][q]
                    print(Value_Get_01)
                    WS_01.update_cell(next_row,q,Value_Get_01)
                    q = q+1   
            q = 0

            i = i + 1
'''
#discordに投稿
#メッセージ/投稿内容編集2
'''

        Fre_01ms_str = str('{:8,d}'.format(free_01m_a))+'(' + str('{:11,d}'.format(Fre_01ms)) + '分)'
        Fre_05ms_str = str('{:8,d}'.format(free_05m_a))+'(' + str('{:11,d}'.format(Fre_05ms)) + '分)'
        Fre_10ms_str = str('{:8,d}'.format(free_10m_a))+'(' + str('{:11,d}'.format(Fre_10ms)) + '分)'
        Fre_15ms_str = str('{:8,d}'.format(free_15m_a))+'(' + str('{:11,d}'.format(Fre_15ms)) + '分)'
        Fre_30ms_str = str('{:8,d}'.format(free_30m_a))+'(' + str('{:11,d}'.format(Fre_30ms)) + '分)'
        Fre_60ms_str = str('{:8,d}'.format(free_60m_a))+'(' + str('{:11,d}'.format(Fre_60ms)) + '分)'
        Fre_03hs_str = str('{:8,d}'.format(free_03h_a))+'(' + str('{:11,d}'.format(Fre_03hs)) + '分)'
        Fre_08hs_str = str('{:8,d}'.format(free_08h_a))+'(' + str('{:11,d}'.format(Fre_08hs)) + '分)'
        Fre_15hs_str = str('{:8,d}'.format(free_15h_a))+'(' + str('{:11,d}'.format(Fre_15hs)) + '分)'
        Fre_24hs_str = str('{:8,d}'.format(free_24h_a))+'(' + str('{:11,d}'.format(Fre_24hs)) + '分)'
        Fre_72hs_str = str('{:8,d}'.format(free_72h_a))+'(' + str('{:11,d}'.format(Fre_72hs)) + '分)'
        Fre_total_str = str('{:11,d}'.format(Fre_total))
        free_to_hour_str = str('{:11,d}'.format(free_to_hour))
        free_to_days_str = str('{:11,d}'.format(free_to_days))

        str_01 = str('{:>7s}'.format('01分加速：'))
        str_02 = str('{:>7s}'.format('05分加速：'))
        str_03 = str('{:>7s}'.format('10分加速：'))
        str_04 = str('{:>7s}'.format('15分加速：'))
        str_05 = str('{:>7s}'.format('30分加速：'))
        str_06 = str('{:>7s}'.format('60分加速：'))
        str_07 = str('{:>7s}'.format('03時間加速：'))
        str_08 = str('{:>7s}'.format('08時間加速：'))
        str_09 = str('{:>7s}'.format('15時間加速：'))
        str_10 = str('{:>7s}'.format('24時間加速：'))
        str_11 = str('{:>7s}'.format('03日加速：'))
        str_12 = str('{:>7s}'.format('合計（分)：'))
        str_13 = str('{:>7s}'.format('合計（時)：'))
        str_14 = str('{:>7s}'.format('合計（日)：'))

'''
#メッセージ/投稿内容編集2
'''
        sentmag_01=input_day_02+'現在のフリー加速の数量は'+'\n'+str_01+Fre_01ms_str+'\n'+str_02+Fre_05ms_str+'\n'+str_03+Fre_10ms_str+'\n'+str_04+Fre_15ms_str+'\n'+str_05+Fre_30ms_str+'\n'+str_06+Fre_60ms_str+'\n'+str_07+Fre_03hs_str+'\n'+str_08+Fre_08hs_str+'\n'+str_09+Fre_15hs_str+'\n'+str_10+Fre_24hs_str+'\n'+str_11+Fre_72hs_str+'\n\n'+str_12+Fre_total_str+'分\n'+str_13+free_to_hour_str+'時間\n'+str_14+free_to_days_str+'日分の加速があります' 
'''
#discord送るためのコード
'''

        discord = Discord(url="")
        discord.post(content=sentmag_01)
'''
#lineへメッセージを送る（送る内容はDiscordと同じ)
'''
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