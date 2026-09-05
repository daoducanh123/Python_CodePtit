n = int(input())
while n > 0:
    string = input()
    if string[-2:] == "86":
        print("YES")
    else:
        print("NO")
    n -= 1