t = int(input())
while t > 0:
    string = input()
    arr = []
    sum = 0
        
    for i in range(0, len(string)):
        if string[i].isdigit():
            sum += int(string[i])
        elif string[i].isalpha():
            arr.append(string[i])

    arr.sort()
    for i in range(0, len(arr)):
        print(arr[i], end="")
    print(sum)

    t-=1