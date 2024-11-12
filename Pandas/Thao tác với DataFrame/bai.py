import pandas as pd
import numpy as np
lst = ['Hello','Flinters','How','Are','You']
df1 = pd.DataFrame(lst)
print(df1)
arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
df2 = pd.DataFrame(arr, columns = ['a','b','c'])
print(df2)
print(df2.iloc[:2, :2]) #Hàm iloc là để truyền vào dòng và cột 
print(df2.iloc[2:3]) # Lấy bắt đầu ở dòng 2 và kết thúc ở dòng 3