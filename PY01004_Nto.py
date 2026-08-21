import math


#BONUS
def SangSoNto(n):
    primes = []
    is_prime = [True] * (n+1)
    is_prime [0] = is_prime[1] = False;
    for i in range (2, int(math.sqrt(n))+1):
        if (is_prime[i]):
            for j in range (i * i, n+1, i):
                is_prime[j] = False

    for i in range(len(is_prime)):
        if is_prime[i] == True:
            primes.append(i)
    return is_prime, primes

    
def ChkSoNto(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def UCLN(a,b):
    while b != 0:
        tmp = a
        a = b
        b = tmp % a
    return a


# main
t = int(input())    
is_prime, primes = SangSoNto(10001)
while t > 0:
    n = int(input())

    cnt = 0
    # Duyeejt số nhỏ hơn n
    for i in range (1, n):
        if UCLN(n,i) == 1: 
            cnt += 1
    if is_prime[cnt]:
        print(f"YES")
    else:
        print(f"NO")
    t -= 1




