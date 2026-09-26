def lathuannghich(x):
    s = str(x)
    return len(s)>=2 and s == s[::-1]

n,m = map(int,input().split())

a = []

for _ in range(n):
    row = list(map(int,input().split()))
    a.append(row)
    
maxtn = -1
for i in range(n):
    for j in range(m):
        val = a[i][j]
        if lathuannghich(val):
            if val > maxtn:
                maxtn = val
                
if maxtn == -1:
    print("NOT FOUND")
else:
    print(maxtn)
    for i in range(n):
        for j in range(m):
            if a[i][j] == maxtn:
                print(f"Vi tri [{i}][{j}]")

        
    
