check = False
Max_Value = 0
while not check:
    number = int(input("Nhap so: "))
    if number == 0:
        check = True
        break
    if number > Max_Value:
        Max_Value = number
if check == True:
    print("GTLN la: ",Max_Value)
