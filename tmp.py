
from collections import deque

n = int(input())

graph = {}
indegree = {}

for _ in range(n):
    a, sign, b = input().split()

    if a not in graph:
        graph[a] = []
        indegree[a] = 0
    if b not in graph:
        graph[b] = []
        indegree[b] = 0

    # Chuyển phép so sánh thành cạnh:
    # a > b: b -> a
    # a < b: a -> b
    if sign == '>':
        u, v = b, a
    else:
        u, v = a, b

    graph[u].append(v)
    indegree[v] += 1

# Đưa các đỉnh có bậc vào bằng 0 vào hàng đợi
q = deque()

for name in indegree:
    if indegree[name] == 0:
        q.append(name)

count = 0

while q:
    u = q.popleft()
    count += 1

    for v in graph[u]:
        indegree[v] -= 1

        if indegree[v] == 0:
            q.append(v)

# Nếu không duyệt được tất cả đỉnh thì có chu trình
if count == len(indegree):
    print("possible")
else:
    print("impossible")
