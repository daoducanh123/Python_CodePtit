mod = 10**9+7

n,k = map(int,input().split())
a = list(map(int,input().split()))
a.sort()

fact= [1] * (n+1)
inv_fact = [1] * (n+1)

for i in range(1,n+1):
    fact[i] = fact[i-1] *i %mod
    
inv_fact[n] = pow(fact[n], mod-2,mod)
for i in range(n,0,-1):
    inv_fact[i-1] = inv_fact[i] * i % mod
    
def c(n,k):
    if k < 0 or n < k :
        return 0
    
    return fact[n] * inv_fact[k] % mod *inv_fact[n-k] % mod
ans = 0

for i in range(n):
    maxcount = c(i,k-1)
    mincount = c(n-i-1,k-1)
    ans= (ans+a[i] * (maxcount-mincount)) % mod
    
print(ans)