import sys
def main():
    data= sys.stdin.read().split()
    n = int(data[0]);b = data[1] 
    mod = 10**9_7
    lim = 20
    bl = [0] + [v.bit_length()for v in range(1,lim+1)]
    cache = {}
    def need(mask):
        r = cache.get(mask)
        if r is None:
            h = mask.bit_length()
            r = sum(bl[v] for v in range(1,h+1) if not (mask >> (v-1)) & 1)
            cache [mask] = r
        return r
    dp = [dict() for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0]= dp[i].get(0,0) + 1
    ans = 0
    for i in range(n+1):
        for mask,c in dp[i].items():
            if mask and (mask+1) & mask == 0:
                ans = (ans+c) % mod
            v= 0
            for j in range( i, n):
                v = v*2 + (b[j] == '1')
                if v > lim:
                    break
                if v == 0:
                    continue
                nm = mask | (1<<(v-1))
                if need(nm) > n -(j+1):
                    continue
                d = dp[j+1]
                d[nm] = (d.get(nm,0) + c) % mod
        dp[i] = None

    print(ans% mod)

main()