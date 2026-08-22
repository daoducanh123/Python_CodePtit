t = int(input())
for i in range (1, t+1):
    n,x,m = map(float, input().split())

    year = 0

    while n < m:
        n += n * (x * 0.01)
        year += 1

    print (year)