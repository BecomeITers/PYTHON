def Res(list, min_value):
    lst = []
    for x in list:
        if x < min_value:
            lst.append(x)
    return lst
def main():
    lst = [1,2,3,4,5,6]
    min_value = int(input("Nhap gia tri min: "))
    print(Res(lst, min_value))
if __name__ == "__main__":
    main()
