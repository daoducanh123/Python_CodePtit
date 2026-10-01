import math

def ChkNto(n):
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
    ok = True
    for i in range(len(s)):
        if ChkNto(int(s[i])):
            if ChkNto(i) == False:
                ok = False
                break
        else:
            if ChkNto(i) == True:
                ok = False
                break
    if ok:
        print("YES")
    else:
        print("NO")
                
            
        

