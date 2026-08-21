test = int(input())
for i in range(0,test):
    number = input()
    arr = []

    for n in number:
        arr.append(int(n))

    for i in range(len(arr)-1, 0, -1):
        if arr[i] >= 5:
            arr[i-1] += 1
        arr[i] = 0

    for i in arr:
        print (i, end = "")

    print()