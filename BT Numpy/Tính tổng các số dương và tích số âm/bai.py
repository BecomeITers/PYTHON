import numpy as np
def check(n):
    if n < 0:
        return False
    return True
arr = np.array([-1,2,-3,4,-5,6])
duong = arr[np.vectorize(check)(arr)]
print(np.sum(duong))
am = arr[~np.vectorize(check)(arr)]
tich = np.prod(am)
print(tich)