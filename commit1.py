import sqlite3
import time
import datetime
import urllib
import pandas as pd
import html5lib

conn = sqlite3.connect('tutorial1.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(TIMESLOT VARCHAR, DELHI VARCHAR, BRPL VARCHAR, BYPL VARCHAR, NDPL VARCHAR, NDMC VARCHAR, MES VARCHAR)')

    c.execute("INSERT INTO stuffToPlot (TIMESLOT , DELHI , BRPL , BYPL , NDPL, NDMC , MES) VALUES (?, ?, ?, ?, ?, ?, ?)",(TIMESLOT , DELHI , BRPL , BYPL , NDPL, NDMC , MES))
    conn.commit()
l='http://www.delhisldc.org/Loaddata.aspx?mode='
m='/1/2017'
d='14'
for d in range (1,30):
    dfs = pd.read_html(str(l+d+m))
    for df in dfs:
        for j in range(1,289):
            c.execute("INSERT INTO stuffToPlot (TIMESLOT , DELHI , BRPL , BYPL , NDPL, NDMC , MES) VALUES (?, ?, ?, ?, ?, ?, ?)",(TIMESLOT , DELHI , BRPL , BYPL , NDPL, NDMC , MES))#(str(df[0:j]) , str(df[1:j]) , str(df[2:j]) , str(df[3:j]) , str(df[4:j]), str(df[5:j]) , str(df[6:j])))
            conn.commit()
create_table()
c.close()
conn.close()
    
