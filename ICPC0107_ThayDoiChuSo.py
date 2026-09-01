# Đề bài: ICPC0107 — THAY ĐỔI CHỮ SỐ

def MIN(a, b, pMin, qMax):
    listA = list(a)

    for i in range(len(a)):
        if a[i] == qMax:
            listA[i] = pMin

    listB = list(b)

    for i in range(len(b)):
        if b[i] == qMax:
            listB[i] = pMin

    resMin = int(''.join(listA)) + int(''.join(listB))

    print(resMin, end=" ")


def MAX(a, b, pMin, qMax):
    listA = list(a)

    for i in range(len(a)):
        if a[i] == pMin:
            listA[i] = qMax

    listB = list(b)

    for i in range(len(b)):
        if b[i] == pMin:
            listB[i] = qMax

    resMax = int(''.join(listA)) + int(''.join(listB))

    print(resMax)


t = int(input())

while t > 0:

    p, q = input().split()

    pMin = str(min(int(p), int(q)))
    qMax = str(max(int(p), int(q)))

    # Đọc X1 và X2
    numbers = input().split()

    if len(numbers) == 2:
        # X1 và X2 cùng một dòng
        a = numbers[0]
        b = numbers[1]
    else:
        # X1 và X2 nằm ở hai dòng
        a = numbers[0]
        b = input().strip()

    MIN(a, b, pMin, qMax)
    MAX(a, b, pMin, qMax)

    t -= 1