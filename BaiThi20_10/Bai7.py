n = int(input())

cnt = [0] * n
for c in range(1,n):
    cnt[c*c%n] += 1
    
    
ans = 0

for a in range(1,n):
    x = a * a % n
    for b in range(a,n):
        y = (x+b*b)%n
        ans+=cnt[y]
        
print(ans)