tu = mau = 0
while True:
    so1 = int(input("Nhap tu so: "))
    so2 = int(input("Nhap mau so: "))
    if so1 != 0 and so2 != 0:
        tu = so1
        mau = so2
    else:
        exit()
    print("Phan so la: ", tu / mau)


