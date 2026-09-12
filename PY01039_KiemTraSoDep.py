t = int (input())
for _ in range(t):
    
    n = int(input())
    s = str(n)
    se = set(s)
    # nếu số đó chỉ có hai chữ số khác nhau
    # 121212-> 12

    ok = True
    if len(se) != 2:
        ok = False

    if ok == False:
        print("NO")
    else:
        for i in range(len(s)-2):
            if s[i] != s[i+2]:
                ok = False
                break
        if ok:
            print("YES")
        else:
            print("NO")        
        
