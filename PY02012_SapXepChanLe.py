n = int(input())
arr = list()
while len(arr) < n:
    arr += list(map(int, input().split()))
#chan tang le giam
s1 = list() # chan
s2 = list() # le

pos = [False] * 1005
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        pos[i] = True
        s1.append(arr[i])
    else:
        s2.append(arr[i])
        
chan = sorted(s1)
le  = sorted(s2,reverse=True)

res = [-1] * 1005
idxChan = 0
idxLe = 0
for i in range(n):
    if pos[i] == True:
        res[i] = chan[idxChan]
        idxChan+=1
    else:
        res[i] = le[idxLe]
        idxLe+=1  
        
for i in range(n):
    print(res[i] , end  = " ")