t = int(input())
for _ in range(t):
    d = dict()
    n = int(input())
    for _ in range(n):
        num = int(input())
        if num in d:
            d[num] += 1
        else:
            d[num] = 1
        
    
    d = dict(sorted(d.items(), key=lambda x: x[0]))
    d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))    
    l = list(d.keys())
    print(l[0])