import math
year = int(input("Nhap nam: "))
day_of_the_week = (year + math.floor((year - 1)/4) - math.floor((year - 1)/100) + math.floor((year - 1)/400)) % 7
days_of_week = ["Chu nhat", "Thu hai", "Thu ba", "Thu tu", "Thu nam", "Thu sau", "Thu bay"]
print('Ngay 1 thang 1 cua nam {0} la ngay {1}'.format(year, days_of_week[day_of_the_week]))