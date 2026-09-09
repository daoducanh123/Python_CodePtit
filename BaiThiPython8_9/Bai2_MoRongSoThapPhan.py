def thuan_nghich(n,k):
    digits = []
    if  n == 0:
        return True
    while n> 0:
        digits.append(n% k)
        n //=k
        
    return digits == digits [::-1]


a,b,M = map(int,input().split())

dem = 0

for x in range (a,b+1):
    ok = True
    for k in range(2,M+1):
        if not thuan_nghich(x,k):
            ok = False
            break
    if ok: 
        dem += 1
        
print(dem)