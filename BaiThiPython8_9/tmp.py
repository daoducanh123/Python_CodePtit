import math

def check (x,y):
    return math.gcd (x,y) == 1

l, r = map(int,input().split())
for i in range(l, r-2):
    for j in range(i+1, r-1):
        for k in range(j+1, r):
            if check(i,j) and check (i,k) and check(j,k):
                print(f"({i}, {j}, {k})")
