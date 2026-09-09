def demuoc(n):
    dem = 0
    for i in range(1, n+1):
        if n % i == 0:
            dem += 1
            
    return dem

t = int (input())
for _ in range(t):
    x = int(input())
    n=1
    max_uoc = 0
    while True:
        so_uoc = demuoc(n)
        
        if so_uoc > max_uoc:
            max_uoc = so_uoc
            
            if n >= x:
                print(n)
                break
        n+=1