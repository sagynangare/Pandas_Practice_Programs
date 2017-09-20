import sqlite3

#conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def tableCreate():
    c.execute("CREATE TABLE IF NOT EXIST stuffToPlot(ID INT, Name VARCHAR, Address VARCHAR, Mobile_No VARCHAR AKA_Name VARCHAR)")
    #conn.commit()
