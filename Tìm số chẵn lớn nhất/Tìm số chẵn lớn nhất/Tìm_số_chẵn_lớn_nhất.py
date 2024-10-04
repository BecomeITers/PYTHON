Max_Positive_Value = 0
i = 0
while i != 3:
    number = int(input("Nhap so: "))
    if number > Max_Positive_Value and number % 2 == 0:
        Max_Positive_Value = number
    if number % 2 != 0:
        print("Phai nhap so chan !")
        exit()
    i += 1
print("Ket qua la: ", Max_Positive_Value)
