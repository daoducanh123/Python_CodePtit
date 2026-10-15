n = int (input())
arr = list(map(float, input().split()))
arr = sorted(arr)
sum = 0
cnt = 0
minVal = arr[0] 
maxVal = arr[-1]
for i in range(len(arr)):
    if arr[i] == minVal or arr[i] == maxVal:
        continue
    else:
       cnt+=1
       sum += arr[i]
res = sum / cnt
print(f"{res:.2f}") 