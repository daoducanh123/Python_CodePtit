import math

def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
    return True

n = int(input())
d = dict()
arr = list(map(int,input().split()))
for a in arr:
    if isPrime(a):
        if a in d:
            d[a] += 1
        else:
            d[a] = 1
for dd in d:
    print(dd, d[dd])