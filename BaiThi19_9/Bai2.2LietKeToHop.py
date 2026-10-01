def Try(pos):
    for j in range (a[pos-1]+1, n-k+pos+1 ,1):
        a[pos] = j
        if pos == k:
            for i in range (1,k+1):
                print(a[i], end = "")
            print()
        else:
            Try(pos+1)
                        
    
t = int (input())
for _ in range(t):
    n,k = map(int,input().split())
    
    a = [0] * (k+1)
    Try(1)