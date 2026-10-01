t = int(input())
for _ in range(t):
    s = input()
    sum = 0
    mul = 1
    cnt = 0

    for i in range (len(s)):
        num = int(s[i])
        if i % 2 == 0:
            sum += num
        else:
            if num != 0:
                mul *= num
                cnt += 1
    print(sum, end = " ")
    if cnt > 0:
        print(mul)
    else:
        print(0)

    