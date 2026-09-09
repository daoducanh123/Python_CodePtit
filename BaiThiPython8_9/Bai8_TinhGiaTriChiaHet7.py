t= int(input())
for _ in range(t):
    n = int(input())
    timthay = False
    for i in range(1001):
        
        if n % 7 == 0:
            print(n)
            timthay = True
            break
        
        if i == 1000:
            break
        
        sodao = int(str(n)[::-1])
        n = n + sodao
    if timthay == False:
        print(-1)
        