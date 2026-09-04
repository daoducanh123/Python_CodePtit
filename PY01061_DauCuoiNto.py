import math

def chkNto(num_n):
    if num_n < 2: return False
    for i in range (2, int(math.sqrt(num_n))+1):
        if num_n % i == 0:
            return False
    return True

t = int(input())
while t > 0:
    string_n = input()
    num1 = 0
    num2 = 0
    for i in range (0,3):
        num1 = num1 * 10 + int(string_n[i])
    
    for i in range (len(string_n)-3,len(string_n)):
        num2 = num2 * 10 + int(string_n[i])
    
    if (chkNto(num1) and chkNto(num2)):
        print("YES")
    else:
        print("NO")
    
    t-=1