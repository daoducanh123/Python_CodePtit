import math
isPrime= [True] * 1001

def Sang():
    isPrime[0] = False
    isPrime[1] = False
    for i in range(2, int(math.sqrt(1000)+1)):
        if isPrime[i]== True:
            for j in range(i * i, 1001, i):
                isPrime[j] = False

# main
Sang()
t = int(input())
for _ in range(t):
    s = input()
    if isPrime[len(s)] == False:
        print("NO")
        continue
        
    cntNto = 0
    cntKoNto = 0
    for i in range(len(s)):
        if isPrime[int(s[i])]: cntNto+=1
        else: cntKoNto +=1
    if cntNto <= cntKoNto:
        print("NO")
        continue
    else:
        print("YES")
        