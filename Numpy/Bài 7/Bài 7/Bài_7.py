import numpy as np
days = np.array(['Thứ Hai', 'Thứ Ba', 'Thứ Tư', 'Thứ Năm', 'Thứ Sáu', 'Thứ Bảy', 'Chủ Nhật'])
sessions = np.array(['Sáng', 'Chiều'])
arr = np.random.randint(0,100,(2,7))
print(arr)

total = np.sum(arr, axis = 0) # axis = 0 là theo chiều cột
max_value = np.argmax(total)
print("Ngay ban duoc nhieu nhat trong tuan: ", days[max_value])

max_sale = 0
buoi = 0
ngay = 0
for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        if arr[i, j] > max_sale:
            max_sale = arr[i, j]
            buoi = sessions[i]
            ngay = days[j]
print("buoi: {0}, ngay: {1}".format(buoi, ngay))

max_buoi = np.sum(arr, axis = 1) # axis = 1 là theo chiều dòng
print("Buoi co khuynh huong ban nhieu hon la: ", sessions[np.argmax(max_buoi)])