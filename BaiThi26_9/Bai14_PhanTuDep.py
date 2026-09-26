t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    
    ans = 0
    
    for i in range(n-1):
        mn = min(a[i], a[i+1])
        mx = max(a[i], a[i+1])
        
        
        while mx > mn*2:
            mn = mn*2
            
            ans+=1
            
    print(ans)