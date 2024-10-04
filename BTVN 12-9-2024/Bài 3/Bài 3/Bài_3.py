lst = []
tup = ()
n = int(input("Nhap n: "))
for x in range(1,n + 1):
    lst.append(x)
for x in range(1, n + 1):
    tup = tup + (x,)
lst += (tup)
print(lst)
print(tuple(lst))
