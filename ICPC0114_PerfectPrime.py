import math

t = int (input())

# Bonus Sangsonto

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
    string_n  =  input()
    num_n = int (string_n)
    chk1 = chkNto(num_n)
    chk2 = sumNto(string_n)
    chk3 = chuSoNto(string_n)
    chk4 = reverseNto(string_n)
    
    if chk1 == True and chk2 == True and chk3 == True and chk4 == True: print ("Yes")
    else: print("No")
    
    
    t-=1