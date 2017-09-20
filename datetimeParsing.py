import pandas as pd
import matplotlib.pyplot as plt
import numpy.random as np
import sys
np.seed(111)

def CreateDataSet(Number = 1):
    Output = []
    for i in range(Number):
        rng = pd.date_range(start='1/1/2009', end = '12/31/2013',freq = 'W-MON')
        data = np.randint(low = 25, high = 1000, size =len(rng))
        status = [1,2,3]
        random_status = [status[np.randint(low=0,high=len(status))] for i in range(len(rng))]
        states = ['GA','FL', 'fl', 'NY','NJ','TX']
        random_states = [states[np.randint(low=0,high=len(states))] for i in range(len(rng))]
        Output.extend(zip(random_states, random_status, data, rng))
    return Output
dataset = CreateDataSet(4)
df =  pd.DataFrame(data=dataset, columns=['State','Status','CustomerCount','StatusDate'])
df.to_csv('DateTime.csv',index = False)
df['CustomerCount'].plot(figsize=(15,5))
plt.show()
print(df.info())
print('*'*30)
print(df.head())
