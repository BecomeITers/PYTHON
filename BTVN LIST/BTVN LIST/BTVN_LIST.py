def Tong(list): 
    sum = 0
    for x in list:
        sum += x
    return sum

def timAm(list):
    value = 0
    for x in list:
        if x < 0:
            value = x
            break
    return value

def timPtAmK(list):
    value = 0
    k = int(input("Nhap gia tri k: "))
    for x in list:
        value = k - len(list)
    return value

def dsChanLe(list):
    lstA = []
    lstB = []
    for x in list:
        if x % 2 == 0:
            lstA.append(x)
        else:
            lstB.append(x)
    return lstA, lstB

def dsNguyenTo(list):
    def isPrime(n):
        if n <= 1:
            return False
        else:
            for x in range(2, int(n ** 1/2)):
                if n % x == 0:
                    return False
        return True
    lst = [x for x in list if isPrime(x)]
    return lst

def xoaK(list):
    k = int(input("Nhap gia tri k : "))
    check = False
    for x in list:
        if x == k:
            check = True
    if check == True:
        list.remove(k)
    return list

def xoaTrungLap(list):
    list.sort() 
    i = 1
    while (i < len(list)):
        if list[i] == list[i - 1]:
            list.pop(i)
        else:
            i += 1
    return list

def SapXep(list):
    lstA = []
    lstB = []
    for x in list:
        if x < 0:
            lstA.append(x)
        else:
            lstB.append(x)
    lstA.sort().extend().lstB.sort(reverse = True)
    return lstA

def UocSoBoiSo(list):
    lstA = []
    lstB = []
    k = int(input("Nhap gia tri k: "))
    for x in list:
        if x == 0:
            continue
        elif k % x == 0:
            lstA.append(x)
    for x in list:
        if x % k == 0:
            lstB.append(x)
    return lstA, lstB

def Thermal(list):
    print("Hay nhap 7 nhiet do tuong ung 7 ngay: ")
    sum = 0
    cnt = 0
    for x in list:
        sum += x
    tb = sum / 7
    for x in list:
        if x > tb:
            cnt += 1
    return cnt

def TimMinMax(list):
    Max_Value = 0
    Min_Value = 999999999999999999
    for x in list:
        if x > Max_Value:
            Max_Value = x
        elif x < Min_Value:
            Min_Value = x
    return Max_Value, Min_Value

def ListSquare(list):
    lst = []
    n = int(input("Nhap n: "))
    for x in range(n + 1):
        if x ** 2 < n:
            lst.append(x ** 2)
    return lst

list = []
n = int(input("Nhap kich thuoc n: "))
for x in range(n + 1):
    list.append(x)

lst = []
i = 0
while i < n:
    num = int(input("Nhap so: "))
    lst.append(num)
    i += 1

print("Tong cac phan tu la: ", Tong(list))
print("Trung binh cong cac phan tu la: ", Tong(list) / len(list))
print("Phan tu am dau tien la: ", timAm(list))
print("Phan tu am o vi tri k la: ", timPtAmK(list))
chan,le = dsChanLe(list)
print("Danh sach phan tu chan la: ", chan)
print("Danh sach phan tu le la: ", le)
print("Danh sach so nguyen to la: ", dsNguyenTo(list))
print("Danh sach sau khi xoa phan tu k la: ", xoaK(lst))
print("Danh sach phan tu ko trung lap la: ", xoaTrungLap(lst))
print("Danh sach phan tu tang dan la: ", list.sort())
print("Danh sach phan tu am giam dan la: ", lst.sort(reverse = True))
print("Danh sach phan tu am tang duong giam la: ", SapXep(lst))
uocso,boiso = UocSoBoiSo(lst)
print('Danh sach uoc so la: {0} va Danh sach boi so la: {1}'.format(uocso, boiso))
print('Co {0} ngay nhiet do lon hon nhiet do trung binh'.format(Thermal(lst)))
ptMax, ptMin = TimMinMax(lst)
print('Phan tu max la {0} va phan tu min la {1}'.format(ptMax, ptMin))
print('List so tu nhien 0 -> n: {0} va List binh phuong < n: {1}'.format(list, ListSquare()))


