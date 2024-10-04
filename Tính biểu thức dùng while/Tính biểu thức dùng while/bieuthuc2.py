n = int(input())
i = 1
mau2 = 1
sum2 = 0
while i <= n:
    i += 1
    mau2 *= i
    sum2 += (1 / mau2)
    print(sum2)
