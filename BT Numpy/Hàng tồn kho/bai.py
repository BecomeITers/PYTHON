import numpy as np
arr = np.array([[1,10,5], [2,5,2.5], [3,3,8]])
sum_so_luong = sum(num[1] for num in arr)
gia_tri = [num[1] * num[2] for num in arr]
print(sum_so_luong)
print(gia_tri)
print(sum(gia_tri))