import numpy as np

def Combine_rooms(arr1, arr2):
    mang1 = arr1[arr1 > 0]
    mang2 = arr2[arr2 > 0]
    arr = mang1
    size = arr.size
    if size < 7:
        size_need = 7 - size
        for x in range(0, size_need):
            arr = np.append(arr, mang2[x])
    return arr

arr1 = np.array([1, 2, -3, 4, 5, 6, -7])
arr2 = np.array([ 8, 9, 10, 11, 12, -13, -14 ])
print(Combine_rooms(arr1, arr2))

