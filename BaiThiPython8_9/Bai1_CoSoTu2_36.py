s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
t = int (input())
for _ in range(t):
    n, b =  map(int, input().split())
    res = []
    # 10 / 2 =  5 du 0 
    # 5 / 2 = 2 du 1
    # 2 / 2 = 1 du 0
    # 1 / 2 = 0 du 1  
    while n > 0:
        idx = n % b
        ss = s[idx]
        res.append(ss)
        n //= b
    for i in range(len(res)-1,-1,-1):
        print(res[i],end = "")
    print()        