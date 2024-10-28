import numpy as np

def replace_col(arr, index_col):
    arr[:, index_col] = 1
    return arr

arr = np.array([(1,2), (3,4), (5,6)])
arr_fix = replace_col(arr, 1)
print(arr_fix)