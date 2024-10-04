rating = float(input("Nhap chi so danh gia: "))
Thuong = 2400 * rating
rate_mapping = {
    0.0: "Unacceptable Performance",
    0.4: "Acceptable Performance",
    0.6: "Meritorious Performance"
    }
if rating in rate_mapping:
    print('{0:>5} {1:>11}'.format('Rating','Meaning'))
    print('{0:>5} {1:>15}'.format(rating, rate_mapping[rating]))
    print("Gia tri thuong la: ", int(Thuong))
elif rating > 0.6:
    print('{0:>5} {1:>11}'.format('Rating','Meaning'))
    print('{0:>5} {1:>15}'.format(rating, "Meritorious Performance"))
    print("Gia tri thuong la: ", int(Thuong))
else:
    print("Vui long nhap lai !")