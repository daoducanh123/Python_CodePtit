t = int (input())
for _ in range(t):
    n = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A = sorted(A)
    B = sorted(B)
    
    ok = True
    minLen = min(len(A),len(B))
    for i in range(minLen):
        if A[i] > B[i]:
            ok = False
            break
    if ok:
        print("YES")
    else:
        print("NO")