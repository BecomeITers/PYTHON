try:
    x = int(input("Nhap so thuc: "))
except ValueError:
    print("Nhap so thuc")
    exit()
fx = 0
if x > 0:
    fx = x ** 2 + 3 * x + 5
elif x <= 0:
    fx = - (x ** 2) - 3 * x - 5
print("Ket qua la: ", fx)