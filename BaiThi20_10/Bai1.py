t = int(input())

for _ in range(t):
     n= int(input())
     a = sorted(map(int,input().split()))
     b = [a[i] - i for i in range(n)]
     b.sort()
     
     mid = b[n // 2] 
     ans = sum(abs(x-mid)for x in b)
     
     print(ans)