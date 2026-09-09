t = int(input())
while t > 0:
    s = input()
    ok = True
    for i in range (len(s)):
        if s[i] != "0" and s[i] != "1" and s[i] != "2":
            ok = False
            break
        
    if ok:
        print("YES")
    else:
        print("NO")
    t-=1