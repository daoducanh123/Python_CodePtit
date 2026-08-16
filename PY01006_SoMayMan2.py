

test = int(input())
while(test > 0):
    ok = True
    num = input()
    cnt4 = 0
    cnt7 = 0
    for x in num:
        if int(x) != 4 and int(x) != 7:
            ok = False
            break

    if ok == True:
        print(f"YES")
    else:
        print(f"NO")

    test -= 1
