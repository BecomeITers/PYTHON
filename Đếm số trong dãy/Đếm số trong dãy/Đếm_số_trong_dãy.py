so_am = 0
while True:
    number = int(input("Nhap so: "))
    if number == 0:
        break
    if number < 0:
        so_am += 1
print("Ket qua la: ",so_am)