diem = input("Nhap diem: ")
grade_mapping = {
    'A+': 4.0,
    'A' : 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C': 2.0,
    'C-': 1.7,
    'D': 1.3,
    'D-': 1.0,
    'F': 0
    }
if diem in grade_mapping:
    print('{0:>5} {1:>11}'.format('Letter','Grade Points')) # {0:>5} là khoảng cách của letter so với gốc
    print('{0:>5} {1:>11}'.format(diem, grade_mapping[diem]))
else:
    print("Diem ko hop le !")