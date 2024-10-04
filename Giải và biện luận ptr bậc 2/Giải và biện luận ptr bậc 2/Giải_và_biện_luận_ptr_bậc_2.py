import math
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
c = int(input("Nhap c: "))
delta = b ** 2 - (4 * a * c)
if delta < 0: 
    print("Phuong trinh vo nghiem")
elif delta == 0:
    x = -b / (2 * a)
    print("x1 = x2 co nghiem: ", x)
else:
    x1 = (- b + math.sqrt(delta)) / (2 * a)
    x2 = (- b - math.sqrt(delta)) / (2 * a)
    print('x1 co nghiem la: {0}'.format(x1))
    print('x2 co nghiem la: {0}'.format(x2))
