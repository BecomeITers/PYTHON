month = 0
while month < 1 or month > 12:
    month = int(input("Nhap thang: "))
if month >= 1 and month <= 3:
    print("Mua xuan")
elif month >= 4 and month <= 8:
    print("Mua ha")
elif month >= 9 and month <= 11:
    print("Mua thu")
else:
    print("Mua dong")
