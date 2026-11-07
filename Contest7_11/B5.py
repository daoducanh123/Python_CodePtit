def solve():
    n= int(input())
    MAX = 9 *len(str(n))
    prime = [True] * (MAX+1)
    prime[0] = prime[1] = False
    for i in range(2,int(MAX**0.5)+1):
        if prime[i] :
            for j  in range(i*i, MAX+1,i):
                prime[j] = False
    digits = list(map(int, str(n)[::-1]))
    
    dp= {(0,0,0):1}
    for d in digits:
        ndp = {}
        
        for (carry,sx,sy),val in dp.items():
            for y in range(10):
                temp = 2*y+carry
                x= (d-temp) % 10
                
                nc = (x+temp) //10
                
                key = (nc,sx+x,sy+y)
                
                ndp [key] = ndp.get(key,0) + val
        dp = ndp
    ans = 0
    
    for (carry,sx,sy),val in dp.items():
        if carry == 0 and prime[sx] and prime[sy]:
            ans+=val
    print(ans)
solve()