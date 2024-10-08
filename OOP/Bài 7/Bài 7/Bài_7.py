class GiaoDich:
    def __init__(self, MaGiaoDich, NgayGiaoDich, DonGia, SoLuong):
        self.MaGiaoDich = MaGiaoDich
        self.NgayGiaoDich = NgayGiaoDich
        self.DonGia = DonGia
        self.SoLuong = SoLuong
    def Nhap(self):
        self.MaGiaoDich = input("Nhap ma giao dich: ")
        self.NgayGiaoDich = input("Nhap ngay giao dich: ")
        self.DonGia = float(input("Nhap don gia: "))
        self.SoLuong = int(input("Nhap so luong: "))
    def Print(self):
        print(f"Ma giao dich: {self.MaGiaoDich}, Ngay giao dich: {self.NgayGiaoDich}, Don gia: {self.DonGia}, So luong: {self.SoLuong}")

class GiaoDichVang(GiaoDich):
    def __init__(self, MaGiaoDich = None, NgayGiaoDich = None, DonGia = None, SoLuong = None, LoaiVang = None):
        super().__init__(MaGiaoDich, NgayGiaoDich, DonGia, SoLuong)
        self.LoaiVang = LoaiVang
    def Nhap(self):
        super().Nhap()
        self.LoaiVang = input("Nhap loai vang: ")
    def ThanhTien(self):
        return self.SoLuong * self.DonGia
    def Print(self):
        print(f"Ma giao dich: {self.MaGiaoDich}, Ngay giao dich: {self.NgayGiaoDich}, Don gia: {self.DonGia}, So luong: {self.SoLuong}, Loai vang: {self.LoaiVang}, Thanh tien: {self.ThanhTien()}")

class GiaoDichTienTe(GiaoDich):
    def __init__(self, MaGiaoDich = None, NgayGiaoDich = None, DonGia = None, SoLuong = None, LoaiTienTe = None, LoaiGiaoDich = None):
        super().__init__(MaGiaoDich, NgayGiaoDich, DonGia, SoLuong)
        self.LoaiTienTe = LoaiTienTe
        self.LoaiGiaoDich = LoaiGiaoDich
    def Nhap(self):
        super().Nhap()
        self.LoaiTienTe = input("Nhap loai tien te: ")
        self.LoaiGiaoDich = input("Nhap loai giao dich (mua/ban): ")
    def ThanhTien(self):
        if self.LoaiGiaoDich == "mua":
            return self.SoLuong * self.DonGia
        elif self.LoaiGiaoDich == "ban":
            return (self.SoLuong * self.DonGia) * 1.05
    def Print(self):
        print(f"Ma giao dich: {self.MaGiaoDich}, Ngay giao dich: {self.NgayGiaoDich}, Don gia: {self.DonGia}, So luong: {self.SoLuong}, Loai tien te: {self.LoaiTienTe}, Loai giao dich: {self.LoaiGiaoDich}, Thanh tien: {self.ThanhTien()}")

gdvang = GiaoDichVang()
gdvang.Nhap()
gdvang.Print()
print("----------------------------------------------------------")
gdtiente = GiaoDichTienTe()
gdtiente.Nhap()
gdtiente.Print()
