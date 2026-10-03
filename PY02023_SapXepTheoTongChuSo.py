t = int(input())

for _ in range(t):
    n = int(input())
    arr = input().split()

    d = dict()
    

    for i in range(len(arr)):
        total = 0

        for j in range(len(arr[i])):
            total += int(arr[i][j])
        d[arr[i]] = total   

    
    d = sorted(d.items(), key=lambda x: int(x[0]))
    d = sorted(d, key=lambda x: x[1])
    
    for x in d:
        print(x[0], end = " ")        