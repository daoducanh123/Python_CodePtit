
t = int(input())
for _ in range(t):
    ok = False    
    num = int(input())
    if num % 7 == 0:
        print(num)
        continue
    for cnt in range(0,1001):
        num = num + int(str(num)[::-1])
        if num % 7 == 0:
            ok = True
            break
        
    if (ok):
        print(num)
    else:
        print(-1)
        