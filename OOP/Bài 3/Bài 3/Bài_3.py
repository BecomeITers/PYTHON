class Number():
    def __init__(self, n):
        self.n = n
        self.lst = []
        
    def DaySo(self):
        for x in range(self.n):
            num = int(input("Nhap so: "))
            self.lst.append(num)
        return self.lst
    
    def Tong(self):
        sum = 0
        for x in self.lst:
            sum += x
        return sum
    
    def TrungBinh(self):
        return self.Tong() / self.n
    
    def TimMax(self):
        Max_Value = self.lst[0]
        for x in self.lst:
            if x > Max_Value:
                Max_Value = x
        return Max_Value
    
    def TimMin(self):
        Min_Value = self.lst[0]
        for x in self.lst:
            if x < Min_Value:
                Min_Value = x
        return Min_Value
    
    def Print(self):
        print(f"Tong: {self.Tong()}, Trung binh: {self.TrungBinh()}, Max: {self.TimMax()}, Min: {self.TimMin()}")

n = int(input("Nhap n: "))
num = Number(n)
num.DaySo()
num.Print()