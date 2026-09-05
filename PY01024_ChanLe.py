t = int(input())
while t >0:

    string_n = input()
    sum = 0
    for i in range(len(string_n)):
        sum += int(string_n[i])

    ok1 = True
    if sum % 10 != 0:
        ok1 = False
    
    ok2 = True
    for i in range(len(string_n)-1):
        so1 =  int(string_n[i])
        so2 = int(string_n[i+1])
        if abs(so1-so2) == 2:
            continue
        else:
            ok2 = False
            break
            
    if ok1 and ok2:
        print("YES")
    else:
        print("NO")
    t-=1
