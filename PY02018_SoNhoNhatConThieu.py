import math
n = int(input())
a = list(map(int,input().split()))

a = sorted(a)
found = False
for i in range(n-1):
    if a[i+1]-a[i] == 1:
        continue
    else:
        found = True
        print(a[i] + 1)
        break
if found == False:
    print(a[n-1]+1)
          