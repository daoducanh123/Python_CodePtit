t = int(input())
for _ in range(t):
    mul = 1
    string  = input()
    for i in range(len(string)):
        number = int (string[i])
        if number != 0:
            mul *= number
    print(mul)