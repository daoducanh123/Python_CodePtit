import math
def prime(n):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i ==0:
            return False
    return True

t = int(input())
for _ in range(t):
    s = input().strip()
    tong = sum(int(x) for x in s)
    if prime(tong):
        print("YES")
    else:
        print("NO")