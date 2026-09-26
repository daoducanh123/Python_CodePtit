import math
def isPrime(n):
    if n < 2: 
        return False
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
    return True

t = int(input())
for _ in range(t):
    
    s = input()
    num = s[-4::]
    n = int(num)

    if isPrime(n):
        print("YES")
    else:
        print("NO")