def XauCon(str):
    str_xoa_trung = set(str)
    str_sort = sorted(str_xoa_trung)
    res = ''.join(str_sort)
    Max_Value = None
    Max_Len = 0
    size = len(res)
    for i in range(size):
        for j in range(i + 1, size + 1):
            if len(res[i:j]) > Max_Len:
                Max_Value = res[i:j]
                Max_Len = len(res[i:j])
    return Max_Value
str = input("Nhap chuoi: ")
print(XauCon(str))