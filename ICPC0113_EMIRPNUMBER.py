def nguyen_to(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def dao_so(n):
    return int(str(n)[::-1])


t = int(input())

for _ in range(t):
    n = int(input())

    for i in range(13, n):
        j = dao_so(i)

        if i < j and j < n and nguyen_to(i) and nguyen_to(j):
            print(i, j, end=" ")

    print()