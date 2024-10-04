try: # Bên trong try là các trường hợp input nhập có thể nhập sai
    a = int(input("Nhap a: "))
    b = int(input("Nhap b: "))
    c = int(input("Nhap c"))
except ValueError: # Nếu sai thì nó sẽ thực thi dòng lệnh trong except
    print("Nhap sai")
    exit()
numbers = [a,b,c]
print("Cac so gtri tuyet doi < 10 la: ")
for x in numbers:
    if abs(x) < 10: 
        print(x)
