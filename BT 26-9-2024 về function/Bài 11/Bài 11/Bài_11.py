def HamBac2(a, b, c):
    lst = []
    delta = (b ** 2) - (4 * a* c)
    if delta == 0:
        x = -b / 2*a
        lst.append(x)
        return lst
    elif delta > 0:
        x1 = (-b + delta ** 0.5) / (2*a)
        x2 = (-b - delta ** 0.5) / (2*a)
        lst.append(x1)
        lst.append(x2)
        return lst
    else:
        return lst
def main():
    a = int(input("Nhap a: "))
    b = int(input("Nhap b: "))
    c = int(input("Nhap c: "))
    print(HamBac2(a, b, c))
if __name__ == "__main__":
    main()
