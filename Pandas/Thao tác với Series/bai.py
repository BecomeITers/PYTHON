import pandas as pd
import numpy as np
data = {'a' : -1.3, 'b' : 11.7, 'd' : 2.0, 'f': 10, 'g': 5}
ser = pd.Series(data, index=['a','c','b','d','e','f']) 
print(ser['a']) 
print(ser[:2])
print(ser[-3:])
a = np.asarray(ser)
print(a)