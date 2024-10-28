import numpy as np

def broadcast(vec, n):
    arr = vec
    for x in range(n - 1):
        vec = np.hstack((vec, arr)) # hstack dùng để nối mảng
    return vec

arr1 = np.array([(2, 3), (4, 5)])
arr2 = np.array([[6], [7]])
arr2_fix = broadcast(arr2, 2)
print(arr1 + arr2_fix)
