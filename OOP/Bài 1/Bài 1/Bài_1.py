class Circle:
    def __init__(self, radius):
        self.radius = radius
    def CV(self):
        return 2 * 3.14 * self.radius
    def DT(self):
        return 3.14 * self.radius * self.radius
    def Print(self):
        print(f"Chu vi: {self.CV()}, Dien tich: {self.DT()}")

radius = int(input("Nhap ban kinh: "))
hinhtron = Circle(radius)
hinhtron.Print()
