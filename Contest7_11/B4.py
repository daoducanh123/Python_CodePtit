def solve():
    import sys
    input = sys.stdin.readline
    
    def multiply(a,b,mod):
        n =len(a)
        c= [[0] *n for _ in range(n)]
        
        for i in range(n):
            for k in range(n):
                if a[i][k] == 0:
                   continue
                x = a[i][k]
                
                for j in range(n):
                    c[i][j] += x * b[k][j]
                    
            for j in range(n):
                c[i][j] %= mod
        return c;
    def multiply_vector(v,a,mod):
        n = len(v)
        res = [0] *n 
        
        for i in range(n):
            if v[i] == 0:
                continue
            for j in range (n):
                res[j] += v[i] * a[i][j]
                
        return [x%mod for x in res]
    
    def count_avoiding (n,s,mod):
        l = len(s)
        pi = [0] *l
        for i in range(1,l):
            j = pi[i-1] 
            while j > 0 and s[i] != s[j] :
                j = pi[j-1]
                
            if s[i] == s[j]:
                j+=1
                
            pi[i] = j
        
        a = [[0] * l for _ in range(l)]
        for i in range(l):
            for c in range(26):
                ch = chr(ord('a')+c)
                
                j = i
                while j >0 and s[j] != ch:
                    j = pi[j-1]
                    
                if s[j] == ch:
                    j+=1
                    
                if j < l:
                    a[i][j] +=1
                    
        v = [0] *l
        v[0] = 1
        
        while n > 0:
            if n &1:
                v = multiply_vector(v,a,mod)
                a= multiply(a,a,mod)
                n>>=1
                
        return sum(v) % mod
    t = int(input())
    
    for _ in range(t):
        n,m = map(int,input().split())
        s= input().strip()
        total = pow(26,n,m)
        avoiding = count_avoiding(n,s,m)
        print((total-avoiding) % m)
        
solve()