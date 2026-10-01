t= int(input())
for _ in range(t):
    n,k = map(int,input().split())
    c=list(map(int,input().split()))
    def check(x):
        a = c[:]
        rows = 0
        for i in range(n):
            rows += a[i]//x
            r = a[i] % x
            if r > 0 and i + 1 < n:
                need = x-r

                if a[i+1] >= need:
                    rows+=1 
                    a[i+1] -= need
            if rows>= k:
                return True
        return False
    
    lo = 1 
    hi = sum(c) //k
    ans = 0


    while lo <= hi:
        mid = (lo+hi) //2
        if check(mid):
            ans = mid
            lo = mid + 1 
        else:
            hi = mid-1

    print(ans*k)