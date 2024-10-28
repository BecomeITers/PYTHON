import Num, random
from My_Package import NghiemBac2 as Nghiem
from My_Package import IncreaseSort as sort1
from My_Package import DecreaseSort as sort2
min_value = int(input("Nhap gia tri min: "))
max_value = int(input("Nhap gia tri max: "))
Num.Num(min_value, max_value)
Num.Print()
print("----------------------------------------------")
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
c = int(input("Nhap c: "))
Nghiem.Value(a,b,c)
print("----------------------------------------------")
lst = [5,8,2,9,1]
sort1.Increase_Sort(lst)
print(lst)
print("----------------------------------------------")
sort2.Decrease_Sort(lst)
print(lst)
