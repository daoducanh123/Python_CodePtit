se = set()
count = 0

while count < 10:
    arr = list(map(int, input().split()))
    count += len(arr)

    for x in arr:
        se.add(x % 42)

print(len(se))