dict = {}
while True:
    name = input("Nhap ho ten: ")
    diem = float(input("Nhap diem: "))
    if diem < 0 or diem > 10:
        print("Invalid")
        exit()
    dict.update({name : diem})
    print("Continue ?")
    print("Yes or No")
    str = input()
    if str == "No":
        break
print(dict)
