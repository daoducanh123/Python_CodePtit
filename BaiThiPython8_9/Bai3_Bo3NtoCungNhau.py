from math import gcd
L,R = map(int,input().split())

for a in range(L,R+1):
    for b in range (a+1, R+1):
        for c in range(b+1, R+1):
            if gcd(a,b) == 1 and gcd(a,c) == 1 and gcd (b,c)==1:
                print(f"({a}, {b}, {c})\n")