from math import isqrt

def solve(a,b,m):
    n = isqrt(m) + 1
    
    baby = {}
    cur = 1
    
    for j in range(n):
        if cur not in baby:
            baby[cur] = j
        cur = cur * a % m
        
    inv = pow(pow(a,n,m),-1,m)
    cur = b
    for i in range(n+1):
        if cur in baby:
            return i * n + baby[cur]
        cur = cur * inv % m
    return -1

t = int(input())
for _ in range(t):
    a,b,m = map(int,input().split())
    print(solve(a,b,m))