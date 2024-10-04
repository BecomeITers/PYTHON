import pandas as pd
Ma = input("Nhap ma: ")
Ten = input("Nhap ten: ")
with open('data.csv', 'a', encoding = 'utf-8') as file:
    file.write(f"{Ma};{Ten}\n")
lst = []
with open('data.csv', 'r', encoding = 'utf-8') as file:
    for data in file:
        data = data.strip()
        if data:
            Ma,Ten = data.split(';')
            lst.append({'Ma' : Ma, 'Ten' : Ten})
MaEdit = input("Nhap ma: ")
nhan_vien = None
for data in lst:
    if data['Ma'] == MaEdit:
        nhan_vien = data
if not MaEdit:
    print("Ko co ma so ma ban kiem")
    exit()
name_edit = input("Nhap ten de sua: ")
nhan_vien['Ten'] = name_edit
nhan_vien.remove(MaEdit)
sapxep_nhanvien = sorted(lst, key = lambda x : x['ma'])
cnt = 0
for data in lst:
    if data['Ten']:
        cnt += 1
print(f"Tong cong co {cnt} nhan vien quan ly")
df = pd.DataFrame(lst)
df[['Ho', 'Ten']] = df['Ten'].str.split(' ', 1, expand = True)
print(df)
