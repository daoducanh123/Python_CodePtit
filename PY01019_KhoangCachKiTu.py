t = int(input())
for _ in range(t):
        
    s1 = input()
    s2 = s1[::-1]
    ok = True

    for i in range(1, len(s1)):
        d1 = abs(ord(s1[i])- ord(s1[i-1]))
        d2 = abs(ord(s2[i])- ord(s2[i-1]))
        if d1 != d2:
            ok = False
            break
        
    if ok:
        print ("YES")
    else:
        print ("NO")