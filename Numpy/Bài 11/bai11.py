import numpy as np

arr1 = np.array([(1,2), (3,4)])
arr2 = np.array([(5,6), (7,8)])
tich = np.dot(arr1, arr2)
hadamard = arr1 * arr2
print(tich)
if hadamard is None:
    print("Ko the tinh")
else:
    print(hadamard)