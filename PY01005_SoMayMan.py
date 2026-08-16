num = input()
cnt4 = 0
cnt7 = 0
for x in num:
    if int(x) == 4:
        cnt4 += 1
    elif int(x) == 7:
        cnt7 += 1

if cnt4 + cnt7 == 4 or cnt4 + cnt7 == 7:
    print(f"YES")
else:
    print(f"NO")