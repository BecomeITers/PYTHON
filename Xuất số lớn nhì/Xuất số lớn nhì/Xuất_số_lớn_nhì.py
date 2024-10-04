a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))
c = int(input("Nhap so c: "))
Max_Second_Value = 0
Max_Value = 0
Min_Value = 99999999999999999
numbers = [a,b,c]
for x in numbers:
    if x > Max_Value:
        Max_Value = x
for x in numbers:
    if x < Min_Value:
        Min_Value = x
for x in numbers:
    if x < Max_Value and x > Min_Value:
        Max_Second_Value = x
print("Ket qua la: ", Max_Second_Value)
