import random
# Bài 1:
sinhvien = {
    "id" : "123",
    "name": "Nguyen Van A",
    "career": "IT"
    }

# Bài 2:
'''100
None
3
['b', 'a', 'c']
[200, 100, 1]
200'''

# Bài 3:
d = {
    'b':200, 
    'a':100, 
    'c':1
     }
d['b'] = 0 - d['b']
d['e'] = 500
del d['b']
print(d)

# Bài 4:
set_a = set(range(201))
print(set_a)

# Bài 5:
def is_Prime(num):
    if num <= 1:
        return False;
    else:
        for x in range(2, int(num ** 1/2) + 1):
            if num % x == 0:
                return False
    return True

set_b = set(x for x in range(10,2001) if is_Prime(x))
print(set_b)

# Bài 6:
set_A = {random.randint(10,2000)}
set_B = {random.randint(10,2000)}
giao = set_A & set_B
hoi = set_A | set_B
hieu = set_A - set_B
hieudx = set_A ^ set_B
print(giao)
print(hoi)
print(hieu)
print(hieudx)

# Bài 7:
dictionary = {
    'a': 1,
    'b': 2,
    'c': 1,
    'd': 3,
    'e': 2
}
result = set(dictionary.values()) # Lấy các giá trị khác nhau
print(result)

# Bài 8: 
dictionary = {
    'a': 1,
    'b': 2,
    'c': 5,
    'd': 8,
    'e': 10
}
result = 0
for x in dictionary.values():
    if x >= result:
        result = x
print(result)

# Bài 9: 
dictionary = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e'
}
Max_Key = float('-inf')
Min_Key = float('inf')
for x in dictionary.keys():
    if x >= Max_Key:
        Max_Key = x
    if x <= Min_Key:
        Min_Key = x
print('Max Key: {0} with Min Key: {1}'.format(Max_Key, Min_Key))