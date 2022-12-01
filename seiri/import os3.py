from cmath import nan
from platform import java_ver
import pandas as pd
import re
import csv
import os
#読み込むcsvファイル指定
dddr = os.getcwd()+'/'
dddf = dddr + 'フォルダ.csv'


df = pd.read_csv(dddf)
count_rows = int(len(df))
input_data = open(dddf, 'r')

i = 0 # index  count_rows
j = 0 # column count_column  

while i < count_rows:
    dir_get = dddr
    num = 0
    for row in i:
        if not re.match('#', row):
            while j < count_column: 
                if num == i:#行数指定
                    split_row = row.rstrip('\n').split(',')
                    l_length = len(split_row)
                    list_b = list(filter(None, split_row))
                    count_column = len(list_b)
                num += 1
                
                dir_value = split_row[j]
                dir_get = dir_get + dir_value+ '/'
            j=j+1
            
            
    input_data.close()
print(dir_get)
i = i+1