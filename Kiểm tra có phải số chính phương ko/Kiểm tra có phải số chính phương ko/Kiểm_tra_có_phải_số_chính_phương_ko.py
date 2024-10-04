import math
a = int(input("Nhap so: "))
scp_new = 0
for x in range(a):
    if x ** 2 == a:
        print("No la so chinh phuong")
        break
    else:
        scp_new = round(math.sqrt(a))
        print("So chinh phuong gan nhat la: ",scp_new ** 2)
        break