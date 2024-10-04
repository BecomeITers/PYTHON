def TrungVi(a,b,c):
    lst = []
    lst.append(a)
    lst.append(b)
    lst.append(c)
    lst.sort()
    return lst[1]
def main():
    a =  int(input("Nhap a: "))
    b =  int(input("Nhap b: "))
    c =  int(input("Nhap c: "))
    print("Ket qua la: ", TrungVi(a,b,c))
if __name__ == "__main__":
    main()

