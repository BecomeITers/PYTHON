# Bài 1:
'''
    a) 9
    b) 5
    c) 5
    d) 2 4
    e) False
    f) 2 4 9 3 5 24 1 4
    g) (2,4,9,3,5)
'''

# Bài 2:
lst = [2,4,9,3,5]
lst[0] = 0 - lst[0]
print(lst)
lst.append(20)
print(lst)
lst.insert(3,0)
print(lst)
lst.pop(4)
print(lst)
lst_copy1 = [2,4,9,3,5]
lst1 = [0,0,0]
lst_copy1.extend(lst1)
print(lst_copy1)
lst_copy2 = [2,4,9,3,5]
lst.copy2.sort(reverse = True)
print(lst_copy2)

# Bài 3:
A = ["3", "27", "5", "123", "9", "1"]
StringCompare = sorted(A) 
print(StringCompare)
IntegerCompare = sorted(A)
print(IntegerCompare)

# Bài 4: 
lstA =  [12,24,35,70,88,120,155]
lstB = []
for index, value in enumerate(lstA): # Hàm enumerate là có thể in ra index và value trong list
    if value == 24 or value == 35 or value == 70 or value == 155:
        lstB.append(value)
lstC = [x for x in lstA if x not in lstB]
# List Comprehension là có thể tạo với x đầu tiên là biểu thức toán còn if là điều kiện để thêm vào list
print(lstC)

# Bài 5:
listA = [1, 2, 3, 1, 2, 5, 6, 7, 8]
i = 1
list.sort()
while i < len(list):
    if list[i] == list[i - 1]:
        list.pop(i)
    i += 1
print(list)
set_a = {1, 2, 3, 1, 2, 5, 6, 7, 8}
set_intersection = set_a & set_a # Đây là hàm để in ra các giao số có nghĩa là xóa các phần tư giống nhau
print(set_intersection)

# Bài 6:
lst = [1,1,1,1,2,2,2,2,3,3,4,5,5]
cnt = 0
value = lst[0]
for x in lst:
    if x == value:
        cnt += 1
    else: 
        print('{0} : {1}'. format(value,cnt))
        value = x
        cnt = 1
print('{0} : {1}'.format(value, cnt))
# Hàm collection này là để đếm số lần xuất hiện của các phần tử trong một iterable
from collections import Counter
lst = [1,1,1,1,2,2,2,2,3,3,4,5,5]
count = Counter(lst)
print(count)

# Bài 7:
n = int(input("Nhap kich thuoc list: "))
lstA = []
lstB = []
i = 0
while i < n:
    num = int(input("Nhap so: "))
    lst.append(num)
    i += 1
while True:
    num = int(input("Nhap so: "))
    if num == -1:
        break
    else:
        lstB.append(num)

# Bài 8:
def XoaTrung(lst):
    i = 1
    while i < len(lst):
        if lst[i] == lst[i - 1]:
            lst.pop(i)
        i += 1
    return lst

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
a = XoaTrung(a)
b = XoaTrung(b)
for x in a:
    for y in b:
        if x == y:
            c.append(x)
print(c)
set_a = {1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89}
set_b = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
set_c = set_a & set_b
print(set_c)