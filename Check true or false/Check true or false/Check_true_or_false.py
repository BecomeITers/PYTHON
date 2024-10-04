import math # Muốn dùng hàm sin và cos thì phải khai báo thư viện math
x = float(input("Nhap gia tri x: "))
BieuThuc = (math.sin(x) ** 2) + (math.cos(x) ** 2) # cos(x) = math.cos(x)
if BieuThuc == 1 :
    print("True")
else:
    print("False")
