from xml.etree.ElementTree import tostring


lstA = [5,6,8,9,-5]
lstB = [-9,5,4,7,8]
lstC = [6,7,8,3,6,46,7,2,-6,-7]

with open('dayso.txt', 'a', encoding = 'utf-8') as file:
    file.write(','.join(map(str, lstA)) + '\n')
    file.write(','.join(map(str, lstB)) + '\n')
    file.write(','.join(map(str, lstC)) + '\n')

def Read():
    lst = []
    try: 
        with open('dayso.txt', 'r', encoding = 'utf-8') as file:
            for x in file:
                numbers = x.strip()
                if numbers:
                    lst.append([int(num) for num in numbers.split(',')]) # Tách các số và chuyển đổi chúng thành integer
    except:
        print("Danh sach ko ton tai")
    return lst

def Print(list):
    if not list:
        print("Danh sach rong")
    else:
        for num in list:
            print(num)

def PrintAm(list):
    lst = []
    if not list:
        print("Danh sach rong")
    else:
        for series in list:
            for num in series:
                if num < 0:
                    lst.append(num)
    return lst

def TBCDuong(list):
    result = 0
    cnt = 0
    for series in list:
        for num in series:
            if num > 0:
                cnt += 1
                result += num
    return float(result / cnt)

def CheckPrime(num):
    if num <= 1:
        return False
    else:
        for x in range(2, int(num * 0.5) + 1):
            if num % x == 0:
                return False
    return True

def CountPrime(list):
    cnt = 0
    for series in list:
        for num in series:
            if CheckPrime(num):
                cnt += 1
    return cnt

def Sum(list):
    sum = 0
    for series in list:
        for num in series:
            if num % 2 == 0 and num % 3 == 0 and num % 4 != 0:
                sum += num
    return sum

def main():
    dayso = Read()
    Print(dayso)
    print("Day so am la: ")
    print(PrintAm(dayso))
    print("Trung binh cong duong la:")
    print(TBCDuong(dayso))
    print(f"Co {CountPrime(dayso)} so nguyen to trong tap tin")
    print("Sum theo dieu kien la: ")
    print(Sum(dayso))

if __name__ == "__main__":
    main()