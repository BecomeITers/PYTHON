from math import sqrt
class ToaDo():
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.colour = colour
    def Print(self):
        print(f"Toa do x {self.x} va toa do y {self.y} va mau sac {self.colour}")
    def TinhTien(self):
        y = 0
        print(f"Toa do x {self.x} va toa do y {y}")
    def TinhTienOxy(self):
        x = 0
        y = 0
        print(f"Toa do tinh tuyen Ox {self.x}, {y}")
        print(f"Toa do tinh tuyen Oy {x}, {self.y}")
    def KhoangCach(self):
        return sqrt(self.x ** 2 + self.y ** 2)
    def KhoangCach2Diem(self, x , y):
        return sqrt((x - self.x) ** 2 + (y - self.y) ** 2)

x = 1
y = 2
colour = "green"
toado = ToaDo(x,y,colour)
toado.Print()
print(toado.KhoangCach())
print(toado.KhoangCach2Diem(3,4))