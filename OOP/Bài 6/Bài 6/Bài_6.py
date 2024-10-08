class MonHoc:
    FILE_NAME = 'dsmh.txt'  # Định nghĩa tên tệp cho môn học

    def __init__(self, ma_mh, ten_mh, so_tiet):
        self.ma_mh = ma_mh
        self.ten_mh = ten_mh
        self.so_tiet = so_tiet

    @classmethod
    def Nhap(cls):
        ma_mh = input("Nhập mã môn học: ")
        ten_mh = input("Nhập tên môn học: ")
        so_tiet = input("Nhập số tiết: ")
        mh = cls(ma_mh, ten_mh, so_tiet)
        with open(cls.FILE_NAME, 'a', encoding='utf-8') as file:
            file.write(f"{ma_mh};{ten_mh};{so_tiet}\n")
        return mh

    @classmethod
    def Read(cls):
        lst = []
        try:
            with open(cls.FILE_NAME, 'r', encoding='utf-8') as file:
                for x in file:
                    x = x.strip()
                    if x:
                        ma_mh, ten_mh, so_tiet = x.split(';')
                        lst.append({'MaMH': ma_mh, 'TenMH': ten_mh, 'SoTiet': so_tiet})
        except FileNotFoundError:
            print(f"Tệp {cls.FILE_NAME} không tồn tại.")
        return lst

    @staticmethod
    def Print(lst):
        if not lst:
            print("Danh sách trống")
        else:
            for x in lst:
                print(f"Mã môn: {x['MaMH']}, Tên môn: {x['TenMH']}, Số tiết: {x['SoTiet']}")


class SV:
    FILE_NAME = 'dssv.txt'  # Định nghĩa tên tệp cho sinh viên

    def __init__(self, cccd, ho_ten, nam_sinh):
        self.cccd = cccd
        self.ho_ten = ho_ten
        self.nam_sinh = nam_sinh

    @classmethod
    def Nhap(cls):
        cccd = input("Nhập số CCCD: ")
        ho_ten = input("Nhập họ tên: ")
        nam_sinh = input("Nhập năm sinh: ")
        sv = cls(cccd, ho_ten, nam_sinh)
        with open(cls.FILE_NAME, 'a', encoding='utf-8') as file:
            file.write(f"{cccd};{ho_ten};{nam_sinh}\n")
        return sv

    @classmethod
    def Read(cls):
        lst = []
        try:
            with open(cls.FILE_NAME, 'r', encoding='utf-8') as file:
                for x in file:
                    x = x.strip()
                    if x:
                        cccd, ho_ten, nam_sinh = x.split(';')
                        lst.append({'CCCD': cccd, 'HoTen': ho_ten, 'NamSinh': nam_sinh})
        except FileNotFoundError:
            print(f"Tệp {cls.FILE_NAME} không tồn tại.")
        return lst

    @staticmethod
    def Print(lst):
        if not lst:
            print("Danh sách trống")
        else:
            for x in lst:
                print(f"CCCD: {x['CCCD']}, Họ tên: {x['HoTen']}, Năm sinh: {x['NamSinh']}")


sv = SV.Nhap()
dsmh = MonHoc.Nhap()
dssv = SV.Read()
dsmh_lst = MonHoc.Read()
SV.Print(dssv)
MonHoc.Print(dsmh_lst)
