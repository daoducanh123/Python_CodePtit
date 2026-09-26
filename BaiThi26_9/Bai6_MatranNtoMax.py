def languyento(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

n,m = map(int,input().split())

a = []

for _ in range(n):
    row = list(map(int,input().split()))
    a.append(row)
    
maxPrime = -1
for i in range(n):
    for j in range(m):
        val = a[i][j]
        if languyento(val):
            if val > maxPrime:
                maxPrime= val
                
if maxPrime == -1:
    print("NOT FOUND")
else:
    print(maxPrime)
    for i in range(n):
        for j in range(m):
            if a[i][j] == maxPrime:
                print(f"Vi tri [{i}][{j}]")

        
    
