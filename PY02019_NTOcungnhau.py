from math import gcd
n = int(input())
arr = list(map(int,input().split()))

arr = sorted(arr)


for i in range(0,n-1):
    for j in range(i+1,n):
        if gcd(arr[i],arr[j])==1:
            x = min(arr[i], arr[j])
            y = max(arr[i], arr[j])
            print(x, y)