from token import MINEQUAL


a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))
c = int(input("Nhap so c: "))
Min_Positive_Number = 99999999999999999999999
number = [a,b,c]
for x in number:
    if x >= 0 and x <= Min_Positive_Number:
        Min_Positive_Number = x
print("Ket qua la: ", Min_Positive_Number)
