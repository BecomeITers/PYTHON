n = int(input("Nhap n: "))
if n == 0:
    print("Vui long nhap lai ")
    exit()
i = 1
sum1 = 0
mau1 = 0
while i <= n:
    mau1 += i
    sum1 += (1 / mau1)
    i += 1
print(sum1)
