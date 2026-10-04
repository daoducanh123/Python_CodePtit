t = int(input())

for _ in range(t):
    n = int(input())
    arr = input().split()
    a = []
    
    for stringNum in arr:
        total = 0
        for s in stringNum:
            num = int(s)
            total += num
        a.append((int(stringNum), total))
    
    # Hãy sắp xếp dãy số theo tổng chữ số tăng dần. Nếu tổng chữ số bằng nhau thì số nào nhỏ hơn sẽ viết trước.
    a = sorted(a, key = lambda x: x[0]) 
    a = sorted(a, key = lambda x: x[1]) 
    for x in a:
        print(x[0], end=" ")

    print()