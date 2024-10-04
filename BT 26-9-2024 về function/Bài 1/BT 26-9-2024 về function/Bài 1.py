def TienTaxi(distance):
    phi_co_so = 4
    return 4 + (distance * 1000 * 0.25 / 140)
def main():
    distance = int(input("Nhap quang duong chay: "))
    print("Gia ve la: ", float(TienTaxi(distance)))
if __name__ == "__main__":
    main()
