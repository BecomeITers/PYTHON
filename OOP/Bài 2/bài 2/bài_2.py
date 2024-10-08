from math import sqrt
class TamGiac():
    def __init__(self, a, b, c, colour):
        self.a = a
        self.b = b
        self.c = c
        self.colour = colour
    def CV(self):
        return self.a + self.b + self.c
    def DT(self):
        p = self.CV() / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
    def Print(self):
        print(f"Colour: {self.colour}, Chu vi: {self.CV()}, Dien tich: {self.DT()}")
    def Check(self):
        if self.a == self.b == self.c:
            print("Tam giac deu")
        elif self.c == sqrt(self.a ** 2 + self.b ** 2):
            print("Tam giac vuong")
        elif self.a == self.b:
            print("Tam giac can")
        else:
            print("Tam giac vuong can")

a = int(input("Nhap gia tri a: "))
b = int(input("Nhap gia tri b: "))
c = int(input("Nhap gia tri c: "))
colour = input("Nhap mau: ")
tamgiac = TamGiac(a,b,c,colour)
tamgiac.Print()