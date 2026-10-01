n,q = map(int,input().split())
diff = [0] * (n+2)


for _ in range (q):
    x,y= map(int,input().split())
    diff [x] ^= 1
    diff[y+1] ^=1

ans= []

cur = 0


for i in range(1,n+1):
    cur ^= diff[i] 
    ans.append(str(cur))
print(" ".join(ans))