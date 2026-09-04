n = int(input())
arr = list(map(int,input().split()))

idx1 = 0
idx2 = idx1+1
cnt = 0
while idx2 < len(arr):
    if arr[idx1] != arr[idx2]: cnt +=1 
    idx1 += 1
    idx2 += 1

print(cnt)