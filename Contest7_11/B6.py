t = int(input())
for _ in range(t):
    n = int(input())
    
    a = list(map(int,input().split()))
    
    ans = 0
    
    for i in range(n-1):
        x,y = sorted([a[i],a[i+1]])
        
        while y  > 2*x:
            x*=2
            ans+=1
            
    print(ans)