from cmath import nan
from platform import java_ver
import pandas as pd
import re
import csv
import os

dddr = os.getcwd()+'/'
dddf = dddr + 'フォルダ.csv'
df = pd.read_csv(dddf)
count_rows = int(len(df))




i=0

print(count_rows)

while i < count_rows:
    j = 0
    


    
    dir_name = df.iat[i, 0]
    dir_pass = dddr+dir_name+'/'
    j = j+1
    while j <  count_columns:
           
            dir_name_01 = df.iat[i,j]
            if not dir_name_01 == '':
                dir_pass = dir_pass + dir_name_01+ '/'
            print(dir_pass)
            j = j+1
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