test = int(input())
fib = [0] * 93
fib[1] = 1
fib[2] = 1
for i in range(3, 93, 1):
    fib[i] = fib[i-1] + fib[i-2]

for t in range(0,test):
    a,b = map(int,input().split())
    for i in range(a,b+1):
        print(fib[i], end = " ")

    print()
