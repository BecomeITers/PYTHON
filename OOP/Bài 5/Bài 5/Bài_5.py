from abc import ABC, abstractmethod
from math import sqrt
from multiprocessing.context import assert_spawning
class Shape(ABC):
    def DT(ABC):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def DT(self):
        return 3.14 * (self.radius ** 2)

class HCN(Shape):
    def __init__(self, CD, CR):
        self.CD = CD
        self.CR = CR
    def DT(self):
        return self.CD * self.CR

class TamGiac(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def DT(self):
        p = (self.a + self.b + self.c) / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

hinhtron = Circle(5)
hcn = HCN(10,5)
tamgiac = TamGiac(10,15,8)
print(hinhtron.DT())
print(hcn.DT())
print(tamgiac.DT())
