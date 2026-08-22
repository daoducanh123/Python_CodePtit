test = int(input())

for t in range (0, test):
    n = int(input())
    print(f"1",end = "")
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                n /= i
                cnt += 1
            print (f" * {i}^{cnt}", end = "")

    if (n > 1):
        print(f" * {int(n)}^{1}", end = "")

    print()