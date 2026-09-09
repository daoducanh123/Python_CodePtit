def lasonguyento(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i ==0:
            return False
        i+=1
        
    return True

t = int(input())

for _ in range(t):
    n = input().strip()
    x = int (n[-4:])
    if lasonguyento(x):
        print("YES")
    else:
        print("NO")