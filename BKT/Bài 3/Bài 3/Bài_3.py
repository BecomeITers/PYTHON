class BatDongSan:
    def __init__(self, maSo, chieuDai, chieuRong):
        self.maSo = maSo
        self.chieuDai = chieuDai
        self.chieuRong = chieuRong
    def DienTich(self):
        return self.chieuDai * self.chieuRong

class DatTrong(BatDongSan):
    def __init__(self, maSo, chieuDai, chieuRong):
        super().__init__(maSo, chieuDai, chieuRong)
        
    def GiaTri(self):
        return self.chieuDai * self.chieuRong * 30000000
    
    def Print(self):
        print(f"Ma so: {self.maSo}, Chieu dai: {self.chieuDai}, Chieu rong: {self.chieuRong}, Gia tri: {self.GiaTri()}")

class Nha(BatDongSan):
    def __init__(self, maSo, chieuDai, chieuRong, soLau):
        super().__init__(maSo, chieuDai, chieuRong)
        self.soLau = soLau
    
    def GiaTri(self):
        return self.chieuDai * self.chieuRong * 60000000 + (self.soLau * 100000000)
    
    def Print(self):
        print(f"Ma so: {self.maSo}, Chieu dai: {self.chieuDai}, Chieu rong: {self.chieuRong}, So lau: {self.soLau}, Gia tri: {self.GiaTri()}")

class KhachSan(BatDongSan):
    def __init__(self, maSo, chieuDai, chieuRong, soSao):
        super().__init__(maSo, chieuDai, chieuRong)
        self.soSao = soSao
    
    def GiaTri(self):
        return self.chieuDai * self.chieuRong * 70000000 + (self.soSao * 50000000)
    
    def Phi(self):
        return self.chieuRong * 5000
    
    def Print(self):
        print(f"Ma so: {self.maSo}, Chieu dai: {self.chieuDai}, Chieu rong: {self.chieuRong}, So sao: {self.soSao}, Gia tri: {self.GiaTri()}, Phi: {self.Phi()}")

class BietThu(BatDongSan):
    def __init__(self, maSo, chieuDai, chieuRong):
        super().__init__(maSo, chieuDai, chieuRong)
    
    def GiaTri(self):
        return self.chieuDai * self.chieuRong * 100000000
    
    def Phi(self):
        return self.chieuRong * 10000
    
    def Print(self):
        print(f"Ma so: {self.maSo}, Chieu dai: {self.chieuDai}, Chieu rong: {self.chieuRong}, Gia tri: {self.GiaTri()}, Phi: {self.Phi()}")

danhSachBatDongSan = [
    DatTrong("DT001", 20, 30),
    Nha("N001", 15, 25, 2),
    KhachSan("KS001", 40, 50, 5),
    BietThu("BT001", 30, 40)
]

print("Danh sach co dien tich > 1000: ")
for batDongSan in danhSachBatDongSan:
    if batDongSan.DienTich() > 1000:
        batDongSan.Print()

print("------------------------------------------")

sum = 0
for batDongSan in danhSachBatDongSan:
    sum += batDongSan.GiaTri()
print("Tong phi kinh doanh: ", sum)
