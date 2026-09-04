import math

t = int (input())

isPrime = [True] * 10**7+1
primes = []

# Bonus Sangsonto
def SangSoNto():
    isPrime[0] = False 
    isPrime[1] = False
    for i in range (2, int(math.sqrt(1e7+1))+1):
        if isPrime[i] == True:
            for j in range (i * i, 1e7+2, i):
             isPrime[j] = False                

    for i in range(len(isPrime)):
        if isPrime[i] == True:
            primes.append(i)
    return isPrime, primes 
    
    
def chkNto(num_n):
    if num_n < 2: return False
    for i in range (2, int(math.sqrt(num_n))+1):
        if num_n % i == 0:
            return False
    return True

def sumNto(string_n):
    sum = 0
    for num in string_n:
        sum += int(num)
    return chkNto(sum)

def chuSoNto(string_n):
    for i in range(0, len(string_n)):
        if (chkNto(int(string_n[i]))== False): return False
    return True

def reverseNto(string_n):
    reverse_Nto = string_n[::-1]
    return chuSoNto(reverse_Nto)




while t > 0:
    # isPrime, primes = SangSoNto()
    string_n  =  input()
    num_n = int (string_n)
    chk1 = chkNto(num_n)
    chk2 = sumNto(string_n)
    chk3 = chuSoNto(string_n)
    chk4 = reverseNto(string_n)
    
    if chk1 == True and chk2 == True and chk3 == True and chk4 == True: print ("Yes")
    else: print("No")
    
    
    t-=1