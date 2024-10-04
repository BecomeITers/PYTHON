so_am = 0
so_duong = 0
so_bang_ko = 0
i = 0
while i < 5:
    number = int(input("Nhap so thuc: "))
    if number < 0:
        so_am += 1
    elif number > 0:
        so_duong += 1
    elif number == 0:
        so_bang_ko += 1
    i += 1
print("Ket qua la: ", so_am, so_duong, so_bang_ko)
