import numpy as np
import time
import sys

l = range(1000)
print(sys.getsizeof(5)*len(l))

array = np.arange(1000)
print(array.size*array.itemsize)



##import pandas as pd
##
##df = pd.read_html("http://www.accuweather.com/en/in/delhi/202396/january-weather/202396?monyr=1/1/2017&view=table")
##
##
##print df
##
