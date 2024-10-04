n = int(input("Nhap n: "))
lstA = []
lstB = []
dict = {}
i = 0
while i < n:
    num1 = int(input("Nhap so trong list A: "))
    lstA.append(num1)
    num2 = int(input("Nhap so trong list B: "))
    lstB.append(num2)
    i += 1
for i in range(n):
    dict[lstA[i]] = lstB[i] # Tạo dictionary với lstA là key còn lstB là value
print(dict)
