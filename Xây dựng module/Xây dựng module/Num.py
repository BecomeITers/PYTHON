import random
lst = []
def Num(min_value, max_value):
    print("Nhap size: ")
    size = int(input())
    for x in range(size):
        num = random.randint(min_value, max_value)
        lst.append(num)

def Print():
    for x in lst:
        print(x)
