n = int(input("Nhap n: "))
i = 1
dict = {}
while i <= n:
    dict.update({i : i ** 2})
    i += 1
print(dict)