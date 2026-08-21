a, K, N = map(int, input().split())


start = K - (a % K)

if a + start > N:
    print(-1)
else:

# a+b = K->2K->3k...
    for b in range(start, N - a + 1, K):
        print(b, end=" ")