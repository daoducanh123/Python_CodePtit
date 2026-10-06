import math
isPrime = [True] * 100001
def Sang():
    isPrime[0] = isPrime[1] = False
    for i in range(2, int(math.sqrt(10000))+1):
        if isPrime[i]== True:
            for j in range(i * i, 100001, i):
                isPrime[j] = False

def Main():
    t = int(input())
    for _ in range(t):
        Sang()
        n = input()
        sum = 0
        for i in range(len(n)):
            num = int(n[i])
            sum += num
        if isPrime[sum] == True:
            print ("YES")
        else: print("NO")        
    
Main()
