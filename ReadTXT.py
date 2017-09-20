import pandas as pd
from numpy import random
import matplotlib.pyplot as plt

names = ['Bob','Jessica','Mary','John','Mel']
random.seed(500)
random_names = [names[random.randint(low = 0, high = len(names))] for i in range(1000)]
births = [random.randint(low = 0, high = 1000) for i in range(1000)]
BabyDataSet = list(zip(random_names, births))
df = pd.DataFrame(data = BabyDataSet, columns = ['Names','Births'])
df.to_csv('Sagar1.txt', index=False, header = False)
df1 = pd.read_csv('Sagar1.txt')
print(df[:10])
print("#****#"*10)
name = df.groupby('Names')
df = name.sum()
print(df)
df['Births'].plot.bar()
plt.show()
#print(df1.head())

#print(random_names[:10])
#print(births[:10])
#print(BabyDataSet[:10])

