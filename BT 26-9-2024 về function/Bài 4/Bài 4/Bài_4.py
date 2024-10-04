def NextPrime(n, max_n):
    def IsPrime(max_n):
        if max_n <= 1:
            return False
        else:
            for x in range(2, int(max_n ** 0.5) + 1):
                if max_n % x == 0:
                    return False
        return True
    Max_Value = None
    for x in range(n + 1, max_n):
        if IsPrime(x):
            Max_Value = x
            break
    return Max_Value
def main():
    n = int(input("Nhap n: "))
    res = NextPrime(n, 9999999999999999)
    print("Ket qua la: ", res)
if __name__ == "__main__":
    main()