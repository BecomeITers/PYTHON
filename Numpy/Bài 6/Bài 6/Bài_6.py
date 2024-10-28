import numpy as np
a = int(input("Nhap gia tri a: "))
b = int(input("Nhap gia tri b: "))
arr = a + (b - a) * np.random.rand(10)
print(arr)
# (b - a) là độ dài của khoảng mà bạn muốn sinh các số ngẫu nhiên
#Cuối cùng, bạn cộng a vào kết quả để dịch chuyển các số từ khoảng (0, b - a) sang khoảng (a, b)