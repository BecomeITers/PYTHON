str = input("Nhap chuoi: ")
cnt = 0
for x in str:
    if x.isalpha():
        cnt += 1
print(cnt)
