import math
isPrime = [True] * 10001
isPrime [0] = False
isPrime [1] = False
for i in range(2, int(math.sqrt(10000) + 1)):
    if isPrime[i] == True:
        for j in range(i * i, 10000, i):
            isPrime[j] = False

n = int(input())
for _ in range(n):
        
    s = input()
    number = int(s[-4::])
    if isPrime[number]:
        print("YES")
    else:
        print("NO")