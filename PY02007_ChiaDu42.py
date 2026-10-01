se = set()
arr = list(map(int,input().split()))
for i in range(len(arr)):
    se.add(arr[i] % 42)
    
print(len(se))