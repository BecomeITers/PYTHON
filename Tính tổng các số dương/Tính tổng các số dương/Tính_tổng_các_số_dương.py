sum = 0
while True:
    number = int(input("Nhap so: "))
    if number != 0:
        if number > 0:
            sum += number
    else:
        break
print("Ket qua: ",sum)
