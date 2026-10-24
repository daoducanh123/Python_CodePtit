
n = int(input())
arr = []

while len(arr) < n:
    arr += list(map(int, input().split()))

chan = []
le = []

for x in arr:
    if x % 2 == 0:
        chan.append(x)
    else:
        le.append(x)

chan.sort()
le.sort(reverse=True)

i = 0
j = 0

for k in range(n):
    if arr[k] % 2 == 0:
        arr[k] = chan[i]
        i += 1
    else:
        arr[k] = le[j]
        j += 1

print(*arr)
