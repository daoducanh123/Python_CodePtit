n = int(input())

a= []

for _ in range(n):
    s = input()

    num = ""

    for c in s:
        if c.isdigit():
            num+= c
        else:
            if num:
                a.append(int(num))
                num = ""

    if num:a.append(int(num))
a.sort()

for x in a:
    print(x)