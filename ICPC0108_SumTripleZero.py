t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    cnt = 0

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            total = a[i] + a[left] + a[right]

            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                cnt += 1
                left += 1
                right -= 1

    print(cnt)
    t -= 1