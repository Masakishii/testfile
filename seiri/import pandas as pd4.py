from cmath import nan
from platform import java_ver
from socket import if_nameindex
import pandas as pd
import re
import csv
import os

dddr = os.getcwd()+'/'
dddf = dddr + 'フォルダ.csv'
df = pd.read_csv(dddf)
count_rows = int(len(df))


f = open(dddf, "r")
reader = csv.reader(f)
data = [ e for e in reader ]
print(data)
f.close()


i=0

print(count_rows)

while i < count_rows:
    data_01 = data[i]
    j = 0
    dir_pass = ''
    #split_row = data.rstrip('\n').split(',')
    #print(split_row)
    ##指定業のリストの数を表示
    #l_length = len(data_01)
    #print(l_length)
    chars = list(filter(None, data[i]))
    ##リストの空白場所削除後のリスト表示
    #print(chars)
    coundd = len(chars)
    #print(coundd)
    ##リストの空白場所削除した後のリストの数表示
    list_b = list(filter(None, chars))
    count_columns = len(list_b)
    while j <  count_columns:

        dir_name_01 = chars[j]
        dir_pass = dir_pass + dir_name_01+ '/'
        
        j = j+1
    
    print(dir_pass)
    i = i+1

#vlo = df.loc[row_number]
#
#
#C_Num_str = str(column_number)
#R_Num_str = str(row_number)
#print(vlo)
#print('bom')
#print('bom' + vlo)
#
#
#strvlo = str(vlo)
#
#
#Get_value = strvlo.replace( '\n' , '' )
#Get_value2 = Get_value.replace( 'Name: '+ R_Num_str + ', dtype: object' , '' )
#Get_value3 = Get_value2.replace(  C_Num_str + '    ' , '' )
#
#print(df_Co_Row)