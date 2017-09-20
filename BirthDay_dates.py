from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd
import sys

names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]
BabyDataSet = list(zip(names, births))
#print(BabyDataSet)
#print("#"*30)
df = pd.DataFrame(data = BabyDataSet, columns = ['Names', 'Births'])
#df.to_csv('Sagar.csv', index = False, header = False)
df1= pd.read_csv('Sagar.csv', names = ['Names', 'Births'])
#print(df)
df1['Births'].plot()
plt.show()
print('**'*50)
print(df1)
