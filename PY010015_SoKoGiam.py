test = int(input())
while test > 0:
    n = input()
    ok = True
    for i in range(len(n)-1):
        if n[i+1] < n[i]:
            ok = False
            break

    if ok == False:
        print("NO")
    else:
        print("YES")

    test-=1