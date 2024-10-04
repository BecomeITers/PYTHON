SoXe = int(input("Nhap so xe: "))
SoNut = 0
while SoXe != 0 :
    Number = SoXe % 10
    SoNut += Number
    SoXe //= 10
print("Ket qua la: ", (SoNut % 10))
