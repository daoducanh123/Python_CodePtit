import math
# sang nto
# Cho ma trận A[] cỡ N*M chỉ bao gồm các số nguyên dương không quá 1000.
def SangSoNto():
    isPrime = [True] * 1001
    primes = list()
    
    isPrime[0] = isPrime[1] = False
    for i in range(2, int(math.sqrt(1000))+1):
        if isPrime[i] == True:
            for j in range(i*i, 1001, i):
                isPrime[j] = False
    for i in range(1001):
        if isPrime[i] == True:
            primes.append(i)
    return isPrime, primes

    

isPrime, primes = SangSoNto() # bonus primes
n,m = map(int,input().split())
a = [[0] * m for _ in range(n)]

# quan trongj
# 3 3
# 1 2 3
# 4 5 6
# 7 8 9

for i in range(n):
    a[i] = list (map(int, input().split()))
    
for i in range(n):
    for j in range(m):
        if isPrime[a[i][j]] == True:
            print(1, end = " ")
        else:
            print(0, end = " ")
    print()