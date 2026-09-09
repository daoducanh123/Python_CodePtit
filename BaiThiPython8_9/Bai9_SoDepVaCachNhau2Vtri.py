t = int(input())

for _ in range(t):
    s = input().strip()
    
    if len(set(s))!=2:
        print("NO")
        continue

    dep  =True
    
    for i in range(len(s)-2):
        if s[i] != s[i+2]:
            dep = False
            break
        
    if dep:
        print("YES")
        
    else:
        print("NO")