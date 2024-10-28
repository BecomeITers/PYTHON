import numpy as np
def is_prime(n):
    if n < 2:
        return False
    else:
        for x in range(2, int(n ** 0.5) + 1):
            if n % x == 0:
                return False
    return True
arr = np.array([2,3,4,5,6,7,8,9,10])
prime_numbers = arr[np.vectorize(is_prime)(arr)]
print(prime_numbers)
print(np.sum(prime_numbers))