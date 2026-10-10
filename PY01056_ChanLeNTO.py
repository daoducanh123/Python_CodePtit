import math
isPrime = [True] * 100005
isPrime[0] = isPrime[1] = False

def Sang():
    for i in range(2, math.sqrt(100090)+1) :
        if isPrime[i] == True:
            for j in range(i*i, 100001, i):
                isPrime[j] = False
                   

t = int(input())
for _ in range(t):
    ok = True
    sum = 0
    string = input()
    for i in range(len(string)):
        number = int(string[i])
        sum += number
        if (number % 2 == 0 and i % 2 == 1) or (number % 2 == 1 and i % 2 == 0):
            ok = False
    if isPrime[sum] and ok == True:
        print("YES")
    else:
        print("NO")