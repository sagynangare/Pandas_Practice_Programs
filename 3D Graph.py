import pandas as pd
from pandas import DataFrame
import datetime
#import pandas.io.data

import matplotlib.pyplot as plt

df = pd.read_csv('ZILL-Z77006_4B.csv',index_col = 'Date', parse_dates = True)
df['H-L'] = df['High']-df.Low
df['100MA'] = pd.rolling_mean(df['Close'], 100)
df['Difference'] = df['Close'].diff()
df[['close', 'High', 'Low','Open','100MA']].plot()
plt.show()
