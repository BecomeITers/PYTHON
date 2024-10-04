def Nhap():
    MaSp = input("Nhap ma san pham: ")
    TenSp = input("Nhap ten san pham: ")
    DonGia = float(input("Nhap don gia san pham: "))

    with open('sanpham.txt', 'a', encoding = 'utf-8') as file:
        file.write(f"{MaSp};{TenSp};{DonGia}\n")
    print("Da them san pham thanh cong")

def Read():
    lst = []
    try:
        with open('sanpham.txt', 'r', encoding = 'utf-8') as file:
            for x in file:
                x = x.strip()
                if x:
                    MaSp,TenSp,DonGia = x.split(';')
                    DonGia = float(DonGia)
                    lst.append({'MaSp' : MaSp, 'TenSp' : TenSp, 'DonGia' : DonGia})
    except:
        print("File ko ton tai")
    return lst

def Print(list):
    if not list:
        print("Danh sach trong")
    else:
        print("Danh sach san pham: ")
        for product in list:
            print(f"Ma san pham: {product['MaSp']}, Ten: {product['TenSp']}, Đon gia: {product['DonGia']}")

def Edit(list):
    MaSpEdit = input("Nhap ma san pham thay doi: ")
    ProductEdit = None
    
    for product in list:
        if product['MaSp'] == MaSpEdit:
            productEdit = product
            break
    
    if not productEdit:
        print(f"Ma {MaSpEdit} ko co ton tai !")
        return

    str = None
    while True:
        print("TenSp or DonGia: ")
        str = input()
        if str == "TenSp":
            break
        elif str == "DonGia":
            break
        

    if str == "TenSp":
        value = input("Nhap gia tri thay doi: ")
        productEdit[str] = value;
    elif str == "DonGia":
        value = float(input("Nhap gia tri thay doi: "))
        productEdit[str] = value;

    with open('sanpham.txt', 'w', encoding = 'utf-8') as file:
        for product in list:
            file.write(f"{product['MaSp']};{product['TenSp']};{product['DonGia']}\n")
    print("Da update san pham")
    
def Delete(list):
    MaSpDelete = input("Nhap ma san pham de xoa: ")
    ProductDelete = None
    for product in list:
        if product['MaSp'] == MaSpDelete:
            ProductDelete = product
            break
    if not ProductDelete:
        print("Ko tim thay san pham de xoa!")
        return
    list.remove(ProductDelete)

    with open('sanpham.txt', 'w', encoding = 'utf-8') as file:
        for product in list:
            file.write(f"{product['MaSp']};{product['TenSp']};{product['DonGia']}\n")
    print("Da update san pham")
    
def Search(list):
    MaSpFind = input("Nhap ma san pham de tim kiem: ")
    ProductFind = None
    for product in list:
        if product['MaSp'] == MaSpFind:
            ProductFind = product
            break
    if not ProductFind:
        print("Ko tim thay!")
        return
    print("Da tim thay san pham ban mong muon")
    print(ProductFind)
    with open('sanpham.txt', 'w', encoding = 'utf-8') as file:
        file.write(f"{product['MaSp']};{product['TenSp']};{product['DonGia']}\n")

def Sort(list):
    if not list:
        print("Danh sach ko co ton tai!")
        return
    ProductSort = sorted(list, key = lambda x: x['DonGia'])
    for product in ProductSort:
        print(f"Ma san pham: {product['MaSp']}, Ten: {product['TenSp']}, Đon gia: {product['DonGia']}")

    with open('sanpham.txt', 'w', encoding = 'utf-8') as file:
        file.write(f"{product['MaSp']};{product['TenSp']};{product['DonGia']}\n")

def main():
    while True:
        print("\n1. Nhap san pham")
        print("\n2. Xem danh sach san pham")
        print("\n3. Thay doi gia tri san pham")
        print("\n4. Xoa san pham")
        print("\n5. Tim san pham")
        print("\n6. Sap xep")
        print("\n0. Thoat")
        lua_chon = input("Chọn chuc nang: ")

        if lua_chon == '1':
            Nhap()
        elif lua_chon == '2':
            danhsach = Read()
            Print(danhsach)
        elif lua_chon == '3':
            danhsach = Read()
            Edit(danhsach)
        elif lua_chon == '4':
            danhsach = Read()
            Delete(danhsach)
        elif lua_chon == '5':
            danhsach = Read()
            Search(danhsach)
        elif lua_chon == '6':
            danhsach = Read()
            Sort(danhsach)
        elif lua_chon == '0':
            break
        else:
            print("Chon lai!")


if __name__ == "__main__":
    main()
