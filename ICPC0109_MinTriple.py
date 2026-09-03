t = int(input())

while t > 0:
    n = int (input())
    a = list (map(int, input().split()))
    
    x = 1000000000-2
    y = 1000000000-1
    z = 1000000000
    
    for i in range (len(a)):
        if a[i] < x:
            z = y
            y = x
            x = a[i]
        elif a[i] < y:
            z = y
            y = a[i] 
        elif a[i] < z:
            z = a[i]
    print(x+y+z)
    
    t-=1