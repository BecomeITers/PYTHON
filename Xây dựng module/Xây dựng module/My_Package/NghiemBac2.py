from math import sqrt

def Value(a,b,c):
    delta = b ** 2 - 4*a*c;
    if delta < 0:
        print("Vo nghiem")
    elif delta == 0:
        res = -b / 2*a
        print(res)
    else:
        res1 = (-b + sqrt(delta)) / 2*a
        res2 = (-b - sqrt(delta)) / 2*a
        print(f"Nghiem thu 1: {res1}, Nghiem thu 2: {res2}")

