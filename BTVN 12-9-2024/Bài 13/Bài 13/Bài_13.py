giogiac = {
    "hoc" : 8,
    "ngu" : 12,
    "the duc" : 2,
    "choi" : 3,
    "di chuyen" : 5
    }
str = input("Nhap hoat dong: ")
time = int(input("Nhap so phut: "))
if str in giogiac:
    giogiac[str] += (time / 60)
else:
    print("Invalid")
print(giogiac)

