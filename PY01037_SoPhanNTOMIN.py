# Cho số nguyên dương X, hãy tìm số phản nguyên tố bé nhất >  X.
def CountUoc(n):
    cnt = 0
    for i in range(1, n + 1):
        if n % i == 0:
            cnt+=1
    return cnt

t = int (input())
for _ in range(t):
    x = int(input())
    
    # 1, 2, 4, 6, 12, 24, …
    maxUoc = -1
    n = 1
    while True:
        cntUoc = CountUoc(n)
        if cntUoc > maxUoc:
            maxUoc = cntUoc
            
            if n >= x:
                print(n)
                break
        n+=1