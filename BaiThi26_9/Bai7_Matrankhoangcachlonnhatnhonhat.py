n,m = map(int, input().split())
a = list()
for i in range(n):
    a.append([0] * m)

maxValue = -1
minValue = 10000

for i in range (n):
    row = list(map(int,input().split()))
    a[i] = row
for i in range (n):
    for j in range(m):
        if a[i][j] > maxValue:
            maxValue = a[i][j]
        if a[i][j] < minValue:
            minValue = a[i][j]
res = maxValue - minValue

ans = []
for i in range (n):
    for j in range(m):
        if a[i][j] == res:
            ans.append((i,j))
if len(ans) > 0:
    print(res)
    for (i, j) in ans:
        print(f"Vi tri [{i}][{j}]")
else:
    print ("NOT FOUND")