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

f.close()


i=0+1
while i < count_rows:
    data_01 = data[i]

    dir_pass = ''

    chars = list(filter(None, data[i]))
    coundd = len(chars)
    list_b = list(filter(None, chars))
    count_columns = len(list_b)
    dir_pass = '/'.join(list_b)+'/'
        

    


    print(dir_pass)
    i = i+1
