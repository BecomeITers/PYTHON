ly_thuyet = -1.0
thuc_hanh = -1.0
check1 = False
check2 = False
while not check1:
    ly_thuyet = float(input("Nhap diem ly thuyet: "))
    if 0 <= ly_thuyet <= 10:
        check1 = True
while not check2:
    thuc_hanh = float(input("Nhap diem thuc hanh: "))
    if 0 <= thuc_hanh <= 10:
        check2 = True
if check1 and check2: # Nếu check1 == check2 thì chạy chương trình
    print("Diem trung binh cong la: ", (ly_thuyet + thuc_hanh) / 2)
