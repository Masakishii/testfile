import tkinter
from  tkinter import *
from datetime import date
from tkinter import messagebox
import sqlite3 #データベースをSQL実行
# データベースに接続する
conn = sqlite3.connect('gakken.db')
c = conn.cursor()
# テーブルの作成
c.execute('''CREATE TABLE IF NOT EXISTS users(name, title, date, staff, content)''')

# データベースへのアクセスが終わったら close する
conn.close()
root = tkinter.Tk()
root.title(u'Gakken PaltyFujiKinuyama')
root.minsize(100, 100)

def import_SQL():
    #入力値を取得する
    value1 = EditBox1.get() #お子様の名前
    value2 = EditBox2.get() #件名
    value3 = EditBox3.get() #日付
    value4 = EditBox4.get() #担当
    value5 = text1.get("1.0",END) #内容
    
    # データベースに接続する
    conn = sqlite3.connect('gakken.db')
    c = conn.cursor()

    # データの挿入
    data = [
    (value1,value2,value3,value4,value5),]
    try:
        c.executemany('INSERT INTO users VALUES(?, ?, ?, ?, ?)', data)
        # 挿入した結果を保存（コミット）する
        conn.commit()
        
        for i in data:
            messagebox.showinfo('登録完了', '{0}を登録しました。'.format(i))
        
        # データベースへのアクセスが終わったら close する
        conn.close()
    except:
        pass


#ラベル
Static1 = tkinter.Label(text=u'お子様の名前')
Static1.pack()
#エントリー
EditBox1 = tkinter.Entry()
EditBox1.pack()
#ここで，valueにEntryの中身が入る
value1 = EditBox1.get()

#ラベル
Static2 = tkinter.Label(text=u'件名')
Static2.pack()
#エントリー
EditBox2 = tkinter.Entry()
EditBox2.pack()
#ここで，valueにEntryの中身が入る
value2 = EditBox2.get()

day = str(date.today())
#ラベル
Static3 = tkinter.Label(text=u'日付')
Static3.pack()
#エントリー
EditBox3 = tkinter.Entry()
EditBox3.insert(tkinter.END,day)
EditBox3.pack()
#ここで，valueにEntryの中身が入る
value3 = EditBox3.get()

#ラベル
Static4 = tkinter.Label(text=u'担当')
Static4.pack()
#エントリー
EditBox4 = tkinter.Entry()
EditBox4.insert(tkinter.END,'大黒知紗')
EditBox4.pack()
#ここで，valueにEntryの中身が入る
value4 = EditBox4.get()

#ラベル
Static5 = tkinter.Label(text=u'内容')
Static5.pack()
text1=tkinter.Text(root,  height=15, width=70)
text1.pack()
value5 = text1.get(END)

# Button
button1 = tkinter.Button(
    root, text='登録',
    command=import_SQL)
button1.pack()

root.mainloop()

