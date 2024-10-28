import numpy as np
arr = np.array([[4,2,7], [1,5,6], [9,8,2]])
sum = np.sum(arr, axis = 1)
indices = np.argsort(sum) #In ra chỉ số sau khi sắp xếp
arr_fix = arr[indices] #Sửa lại mảng theo đúng yêu cầu
print(arr_fix)