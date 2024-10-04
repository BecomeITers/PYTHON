str1 = input("Nhap chuoi: ")
str2 = input("Nhap chuoi de check: ")
size = len(str1)
res = str1[::-1] # Đây là hàm để reverse (str1[start:stop:step]) và nếu để start và stop là trống tự động là đầu và chuỗi ký tự
if res == str2:
    print("True")
else:
    print("False")
