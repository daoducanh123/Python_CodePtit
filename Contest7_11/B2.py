n,m = map(int,input().split())

a = [] 
for i in range(n):
    a.append(list(map(int,input().split())))
    
def is_prime(x):
    if x < 2:
        return False
    
    for i in range(2,int(x**0.5)+1):
        if x %i ==0:
            return False
    return True
max_prime = -1

for i in  range(n):
    for j in range(m):
        if is_prime(a[i][j]):
            max_prime=max(max_prime,a[i][j])
if max_prime==-1:
    print("NOT FOUND")
    
else:
    print(max_prime)
    for i in range(n):
        for j in range(m):
            if a[i][j] == max_prime:
                print(f"Vi tri [{i}][{j}]")
    