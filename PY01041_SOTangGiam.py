t = int(input())
for _ in range(t):
    s = input()
    if len(s) < 3:
        print("NO")
        continue
    l = 0
    r = len(s)-1
    # trai tang
    while l <= len(s)-2 and s[l] < s[l+1]:
        l +=1
        
    # check
    if l == 0 or l == len(s)-1:
        print("NO")
        continue
    
    # phai giam
    while r >= 1 and s[r] < s[r-1]:
        r -=1
    
    if l == r and l != 0 and r != len(s)-1:
        print("YES" )
    else:
        print("NO")