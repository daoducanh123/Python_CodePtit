P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
p = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","_","."]
#  P[(i+K)%28]
while True:
    a = input().split()
    if int(a[0]) == 0:
        break
    else:
        k = int(a[0])
        string = a[1]
        
    res = ""
    for s in string:
        i = P.index(s)
        
        res += P[(i+k) % 28]
    
    revRes = res[::-1]
    print(revRes)