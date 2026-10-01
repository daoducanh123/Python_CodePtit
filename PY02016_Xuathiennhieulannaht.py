t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    count = [0] * 1000001
    
    ok = False
    
    maxCount = -1
    maxValue = -1
    for i in range (len (arr)):
        count[arr[i]] += 1
        if count[arr[i]] > maxCount:
            maxValue = arr[i]
            maxCount = count[arr[i]]
    if maxCount > n//2:
        print (maxValue)
    else:
        print("NO")