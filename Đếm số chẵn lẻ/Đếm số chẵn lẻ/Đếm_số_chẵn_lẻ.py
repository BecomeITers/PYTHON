a = int(input("Nhap so: "))
so_chan = 0
so_le = 0
if a <= 10000 and a >= 99999:
    print("Nhap lai !")
    exit()
while a != 0:
    number = a % 10
    if number % 2 == 0:
        so_chan += 1
    else:
        so_le += 1
    a //= 10
print('{0} so chan va {1} so le'.format(so_chan,so_le))