n = int(input())
arr = list(map(int, input().split()))

stack = [] # list để làm stack  python ko có

for x in arr:
    if len (stack) > 0 and (stack[-1] + x) % 2 == 0:
        stack.pop()
    else:
        stack.append(x)
print(len(stack))

# 5
# 2 3 4 5 6

# stack 
# 6
# 5 
# 4
# 3
# 2