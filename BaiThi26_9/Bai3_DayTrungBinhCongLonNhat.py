n = int(input())
a = list(map(int,input().split()))

maxValue = max(a)
curLen = 0
maxLen = -1

for i in range(n):
    if a[i] == maxValue:
        curLen+=1
        if curLen > maxLen:
            maxLen = curLen
    else:
        curLen = 0
print(maxLen)