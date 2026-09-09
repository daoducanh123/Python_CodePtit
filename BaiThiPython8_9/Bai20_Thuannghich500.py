t = int(input())
for _ in range(t):
    n = input().strip()
    
    tong = sum(int(x) for x in n )
    s = str(tong)
    if len(s) > 1 and s == s[::-1]:
        print("YES")
    else:
        print("NO")