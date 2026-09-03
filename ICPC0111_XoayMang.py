t = int(input())
while t > 0:

    listInput = list(map(int, input().split()))
    n = listInput[0]
    d = listInput[1]
    
    a = list(map(int, input().split()))
    
    for i in range(d, len(a)):
        print(a[i], end = " ")
        
    for i in range (0, d):
        print(a[i], end = " ")
    
    print()
    t-=1