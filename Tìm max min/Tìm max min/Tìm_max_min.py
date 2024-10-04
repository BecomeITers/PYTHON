try:
    a = int(input("Nhap a: "))
    b = int(input("Nhap b: "))
    c = int(input("Nhap c: "))
    d = int(input("Nhap d: "))
    e = int(input("Nhap e: "))
except ValueError:
    print("Phai nhap so thuc")
    exit()
numbers = [a,b,c,d,e]
ValueMax = 0
ValueMin = 99999999999
for x in numbers:
    if x > ValueMax:
        ValueMax = x
    elif x < ValueMin:
        ValueMin = x
print("Max la: ", ValueMax)
print("Min la: ", ValueMin)
