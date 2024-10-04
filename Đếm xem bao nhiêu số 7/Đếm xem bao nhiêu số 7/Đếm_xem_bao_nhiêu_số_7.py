so = int(input("Nhap so: "))
count = 0
while so != 0:
    number = so % 10
    if number == 7:
        count += 1
    so //= 10
print("Ket qua la: ", count)
