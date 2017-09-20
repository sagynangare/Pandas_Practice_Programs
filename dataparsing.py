import pandas as pd
from pandas import DataFrame
import datetime
import sqlite3

def parse_table():
    df = pd.read_table('DataSet.txt', index_col=0, sep=",", escapechar='#',  parse_dates = [4], names=['index', 'Item', 'Date'])
    for line in df:
       line=line.strip().rstrip(',')
       record = frozenset(line.split(','))
       yield record
       
       print(line)
    print(df)
        

parse_table()
