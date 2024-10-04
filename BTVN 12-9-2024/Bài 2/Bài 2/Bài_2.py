lst = []
while True:
    str = input()
    lst.appned(str.split(","))
    get = input("Continue ?") 
    if get == "no":
        break;
print(sorted(lst, key = lambda x:(x[0],x[1],x[2])))
