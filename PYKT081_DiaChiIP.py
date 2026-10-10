t = int(input())
for _ in range (t):
    string = input().strip()
    arrString = string.split(".")

    ok = True
    cnt = 0
    for i in range(len(arrString)):
        if arrString[i].isdigit():
            cnt+=1
            num = int(arrString[i])
            if num > 255 or num < 0:
                ok = False
                break
    
    if ok and cnt == 4:
        print("YES")
    else:
        print("NO")