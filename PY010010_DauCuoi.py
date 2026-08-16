test = int(input())
while (test > 0):
    str = input()
    num1 = int(str[0] * 10) + int(str[1])
    num2 = int(str[-2]*10) + int(str[-1])

    if num1 == num2:
        print(f"YES")
    else:
        print(f"NO")


    test -=1