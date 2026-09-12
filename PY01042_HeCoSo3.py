t = int(input())
for _ in range(t):
    s = input()
    ok = True
    for i in range(len(s)):
        if s[i] not in "012":
            ok = False
            break
        
    if ok:
        print("YES")
    else:
        print("NO")