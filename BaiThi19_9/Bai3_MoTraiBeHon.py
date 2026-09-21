t = int(input())
for _ in range(t):
    n =int (input())
    a = list(map(int,input().split()))

    stack = []
    ans = []

    for i in range(n):
        while stack and a [stack[-1]] <= a[i]:
            stack.pop()
        
        if not stack:
            ans.append(i+1)
        else:
            ans.append(i-stack[-1])
            
        stack.append(i)
        
    print(*ans)