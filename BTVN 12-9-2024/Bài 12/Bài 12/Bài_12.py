str = input()
dict = {}
for x in str:
    if x.isalpha():
        if x in dict:
            dict[x] += 1
        else:
            dict[x] = 1
print(dict)
