year = int(input("Nhap nam: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('{0} la nam nhuan'.format(year))
else: 
    print("Ko phai la nam nhuan")
