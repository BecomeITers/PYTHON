import pandas as pd
import random
lst1 = random.choices(range(1,4), k = 100)
lst2 = random.choices(range(1,3), k = 100)
lst3 = random.choices(range(10000, 30000), k = 100)
s1 = pd.Series(lst1)
s2 = pd.Series(lst2)
s3 = pd.Series(lst3)
print(s1)
print(s2)
print(s3)
print("------------------------------------------------")
res = pd.concat([s1,s2,s3], axis = 1)
print(res)
print("------------------------------------------------")
bigcolumn = pd.concat([s1,s2,s3], ignore_index=True).to_frame(name="bigcolumn")
# Tham số ignore_index=True là cho phép bỏ qua các chỉ số (index) ban đầu của Series hoặc Dataframe để kết hợp thành 1 Dataframe mới
print(bigcolumn)
print("------------------------------------------------")
bigcolumn.reset_index(drop=True, inplace=True) # Đặt lại chỉ mục từ 0 đến 299
print(bigcolumn)