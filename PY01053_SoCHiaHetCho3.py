t = int(    input())
for _ in range(t):
    sum = 0
    string = input()
    for i in range(len(string)):
        number = int(string[i])
        sum += number
    if sum % 3 == 0:
        print("YES")
    else:
        print("NO")