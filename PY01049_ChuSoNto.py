import math
isPrime = [True] * 100005
isPrime[0] = isPrime[1] = False

def Sang():
    for i in range(2, int(math.sqrt(100000))+1) :
        if isPrime[i] == True:
            for j in range(i*i, 100001, i):
                isPrime[j] = False
     
def Chk1(string):
    return isPrime[len(string)]
def Chk2(string):
    cntPrime = 0
    cntNotPrime = 0
    for i in range(len(string)):
        number = int(string[i])
        if isPrime[number]:
            cntPrime += 1
        else:
            cntNotPrime += 1
    return cntNotPrime < cntPrime
    
#main
Sang()
t = int(input())
for _ in range(t):
    string = input()
    if Chk1(string) and Chk2(string):
        print("YES")
    else:
        print("NO")