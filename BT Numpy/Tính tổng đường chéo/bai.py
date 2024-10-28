import numpy as np
sum = 0
matrix = np.array([[1,2,3], [4,5,6], [7,8,9]])
if len(matrix[0]) != len(matrix[1]):
    print("Ko phai la ma tran vuong")
else:
    for i in range(len(matrix)):
        sum += matrix[i][i]
    print(sum)