try:
    str = input("Nhap chuoi so: ")
    lst = str.split(",") # split là loại bỏ dấu ","
    tup = tuple(lst);
    print(lst)
    print(tup)
except:
    print("Error")