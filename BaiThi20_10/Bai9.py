from math import gcd
def solve (a,b,c,d,m):
    if m == 1:
        return 0
    
    e = pow (c,d)
    
    return pow(a,b*e,m)

t = int(input())
for _ in range(t):
    a,b,c,d,m = map(int,input().split())
    
    print(solve(a,b,c,d,m))