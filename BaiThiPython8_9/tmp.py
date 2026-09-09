t = int(input())

ans = []

# i là nửa đầu của số thuận nghịch
for i in range(1, 1000):

    s = str(i)

    # Tạo số thuận nghịch
    s = s + s[::-1]

    # Kiểm tra toàn chữ số chẵn
    ok = True

    for c in s:
        if c not in "02468":
            ok = False
            break

    if ok:
        ans.append(int(s))


while t > 0:

    n = int(input())

    for x in ans:
        if x >= n:
            break

        print(x, end=" ")

    print()

    t -= 1