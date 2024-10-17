class DiaChi():
    def __init__(self, soNha, tenDuong, tenQuan, thanhPho):
        self.soNha = soNha
        self.tenDuong = tenDuong
        self.tenQuan = tenQuan
        self.thanhPho = thanhPho
    def __str__(self):
        return f"{self.soNha}, {self.tenDuong}, {self.tenQuan}, {self.thanhPho}"

class NhanVien():
    def __init__(self, hoTen, ngaySinh, diaChi):
        self.hoTen = hoTen
        self.ngaySinh = ngaySinh
        self.diaChi = diaChi
    def InThongTin(self):
        print(f"Ho ten: {self.hoTen}, Ngay sinh: {self.ngaySinh}, Dia chi: {self.diaChi}")

class NVSX(NhanVien):
    def __init__(self, hoTen, ngaySinh, diaChi, luongCB, soSP):
        super().__init__(hoTen, ngaySinh, diaChi)
        self.luongCB = luongCB
        self.soSP = soSP
    def TinhLuong(self):
        return self.luongCB + self.soSP * 5000
    def InThongTin(self):
        super().InThongTin()
        print(f"Luong CB: {self.luongCB}, So SP: {self.soSP}, Thanh tien: {self.TinhLuong()}")

class NVVP(NhanVien):
    def __init__(self, hoTen, ngaySinh, diaChi, soNgayLamViec):
        super().__init__(hoTen, ngaySinh, diaChi)
        self.soNgayLamViec = soNgayLamViec
    def TinhLuong(self):
        return self.soNgayLamViec * 100000
    def InThongTin(self):
        super().InThongTin()
        print(f"So ngay lam viec: {self.soNgayLamViec}, Thanh tien: {self.TinhLuong()}")

diachi1 = DiaChi("123", "Main St", "Dong Da", "Hanoi")
nhanvien = NhanVien("Nguyen Van A", "1985-05-20", diachi1)
nvsx = NVSX("Nguyen Van B", "1990-08-15", diachi1, 3000000, 150)
diachi2 = DiaChi("234", "Main St", "Q7", "TPHCM")
nvvp = NVVP("Nguyen Van C", "2000-08-15", diachi2, 30)

print("Thong tin nhan vien:")
nhanvien.InThongTin()
print("\nThong tin nhan vien san xuat:")
nvsx.InThongTin()
print("\nThong tin nhan vien van phong:")
nvvp.InThongTin()
