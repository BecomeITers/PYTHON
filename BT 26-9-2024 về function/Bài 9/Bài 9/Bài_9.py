def CheckStar(kwh_max, kwh_lable):
    res = float(kwh_max / kwh_lable)
    if res < 3:
        return True
    return False
def main():
    kwh_max = int(input("Nhap dien nang tieu thu max: "))
    kwh_lable = int(input("Nhap dien nang tieu thu tren nhan: "))
    if CheckStar(kwh_max, kwh_lable):
        print("Tiet kiem dien nang")
    else:
        print("Ko tiet kiem dien nang")
if __name__ == "__main__":
    main()
