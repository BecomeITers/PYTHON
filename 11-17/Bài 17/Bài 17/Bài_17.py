def XauCon(str):
    lst = []
    size = len(str)
    for i in range(size):
        for j in range(i + 1, size + 1):
            lst.append(str[i:j])
    return lst
str = input("Nhap chuoi: ")
print(XauCon(str))