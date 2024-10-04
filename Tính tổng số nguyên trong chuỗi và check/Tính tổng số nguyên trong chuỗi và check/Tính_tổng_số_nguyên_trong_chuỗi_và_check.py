so = -1
while so <= 0:
    so = int(input("Nhap so: "))
sum = 0
while so != 0:
    sum += so % 10
    so //= 10
print("ket qua la: ",sum)
