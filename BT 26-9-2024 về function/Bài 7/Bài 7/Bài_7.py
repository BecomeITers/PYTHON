def Check(kwh):
    if kwh < 10:
        return True
    return False
def main():
    kwh = int(input("Nhap so kwh: "))
    print(Check(kwh))
if __name__ == "__main__":
    main()