def ChuyenDoi(str):
    str_edit = str.lower()
    str_edit = str_edit.strip()
    str_edit = str_edit.split(' ')
    res = None
    for i in range(len(str_edit)):
        str_edit[i] = str_edit[i][0].upper() + str_edit[i][1:] # Đây là viết hoa ký tự đầu tiên trong vòng lặp for
    res = ' '.join(str_edit)
    return res
def main():
    str = input("Nhap chuoi: ")
    print(ChuyenDoi(str))
if __name__ == "__main__":
    main()
