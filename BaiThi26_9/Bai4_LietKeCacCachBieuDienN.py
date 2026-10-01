t = int(input())
for _ in range(t):
    n = int(input())
    ans = []
    
    def quay_lui(tongconlai, giatrilonnhat, cachhientai):
        if tongconlai == 0:
            chuoi = "(" + " ".join(map(str, cachhientai)) + ")"
            ans.append(chuoi)
            return
        
        gioihan= min(tongconlai,giatrilonnhat)
        for i in range(gioihan, 0, -1):
            quay_lui(tongconlai - i, i, cachhientai + [i])
        
    quay_lui(n,n,[])
    
    print(len(ans))
    
    print(*ans)