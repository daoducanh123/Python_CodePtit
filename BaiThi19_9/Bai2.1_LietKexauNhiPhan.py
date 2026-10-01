def Try():
    for j in range(0,2):
        a.append(j)
        if len(a) == n:
            for aa in a:
                print(aa, end = "")
            print()
        else:
            Try()
        a.pop()
   
    
t = int (input())
for _ in range(t):
    n = int(input())
    
    a = []
    Try()