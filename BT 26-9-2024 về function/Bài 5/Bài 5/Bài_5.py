def Check(str):
    check1 = False
    check2 = False
    if len(str) >= 8:
       for char in str:
           if char.isalpha():
                check1 = True
           if char.isupper():
                check2 = True
    if check1 and check2:
        return True
    return False
def main():
    str = input("Nhap chuoi: ")
    print(Check(str))
if __name__ == "__main__":
    main()
               
