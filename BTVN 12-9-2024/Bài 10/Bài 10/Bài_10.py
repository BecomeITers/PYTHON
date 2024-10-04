str = input()
cnt1 = 0
cnt2 = 0
for x in str:
    if x.isdigit():
        cnt2 += 1
    elif x.isalpha():
        cnt1 += 1
print(cnt1, cnt2)
