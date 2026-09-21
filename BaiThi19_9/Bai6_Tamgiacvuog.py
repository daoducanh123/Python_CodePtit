def s(a,b):
    ans= 0
    
    for m in range(1,min(b,a-1)+1):
        c=  a-m+1
        r1=min(m,a-m)
        r2=min(m-1,a-m)
        h += r1*c-r1*(r1+1)//2
        h+=r2*c -r2*(r2+1)//2
        
        ans += (b-m+1)*h
    return ans

t = int(input())

for _ in range(t):
    x,y=map(int,input().split())
    ans = 0
    
    for d in range(1,min(x,y)+1):
        ans+=4 *(x-d+1)*(y-d+1)
        ans +=2 ** s(x,y)
        ans+=2 *s(y,x)
        
        print(ans)