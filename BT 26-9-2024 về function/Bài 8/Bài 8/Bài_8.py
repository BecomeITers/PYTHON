def Star(kmh):
    if kmh < 2: 
        return 5
    elif kmh >= 2 or kmh < 4:
        return 4
    elif kmh >= 4 or kmh < 6:
        return 3
    elif kmh >= 6 or kmh < 10:
        return 2
    else:
        return 1
def main():
    kmh = int(input("Nhap so kmh: "))
    print(Star(kmh))
if __name__ == "__main__":
    main()
