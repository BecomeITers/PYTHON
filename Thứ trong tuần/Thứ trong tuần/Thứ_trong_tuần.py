thu = 0
while thu < 1 or thu > 7:
    thu = int(input("Nhap thu: "))
thu_mapping = {
    1 : "Sunday",
    2 : "Monday",
    3 : "Tuesday",
    4 : "Wensday",
    5 : "Thursday",
    6 : "Friday",
    7 : "Saturday"
    }
if thu in thu_mapping:
    print(thu_mapping[thu])