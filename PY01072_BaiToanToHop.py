n,k = map(int,input().split())
visited = [False] * 1001

#sorted
inputList = list(map(int,input().split()))
inputList = sorted(inputList)

arr = list()
arr.append(-1) # trừ 1

for i in range (n):
    if visited[inputList[i]] == False:
        visited[inputList[i]] = True
        arr.append(inputList[i])
n = len(arr)-1 # bỏ trừ 1
     
# arr = [-1, 1,2,3,4,5]

a = [0] * (k+1)
# a = [0,  0,0,0]
def Try (pos):
    for value in range(a[pos-1] + 1, n-k+pos+1):
        a[pos] = value
        if pos == k:
            for i in range (1, k+1):
                vitri = a[i]
                print(f"{arr[vitri]}", end = " ")
            print()
        else:
            Try(pos+1)
            
Try(1)

