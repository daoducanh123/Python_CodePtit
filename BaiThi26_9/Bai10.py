import sys

dulieu = sys.stdin.read().split()
if dulieu:
    n = int(dulieu[0])
    caccap = []
    idx = 1 
    for _ in range(n):
        x= int(dulieu[idx])
        y =int(dulieu[idx+1])
        caccap.append((x,y))
        idx += 2
        
        
    tapy = sorted(list(set(p[1] for p in caccap)))
    anhxay = {val:i+1 for i, val in enumerate(tapy)}
    m = len(tapy)
    
    
    dp = [1] * n
    phantu = [(i, caccap[i][0], anhxay[caccap[i][1]]) for i in range(n)]
    bit = [0] * (m + 1)
    
    def capnhat(vitri, giatri):
        while vitri <= m:
            if giatri > bit[vitri]:
                bit[vitri] = giatri
            vitri += vitri & (-vitri)
            
    def laymax(vitri):
        ketqua = 0
        while vitri>0:
            if bit[vitri] > ketqua:
                ketqua = bit[vitri]
            vitri -= vitri & (-vitri)
        return ketqua
    def xoabit(vitri):
        while vitri <= m:
            bit[vitri] = 0
            vitri += vitri & (-vitri)
    def chiadetri(trai,phai):
        if trai >= phai:
            
            return
        giua = (trai + phai) // 2
        chiadetri(trai,phai)
        
        nuatrai = sorted(phantu[trai:giua + 1], key = lambda item:item[1])
        nuaphai = sorted (phantu[giua+1:phai+1], key = lambda item:item[1])
        j = 0
        dathem = []
        
        for chisogoc, xphai, yphai in nuaphai:
            while j < len(nuatrai) and nuatrai[j][1] < xphai:
                goct, xtrai, ytrai = nuatrai[j]
                capnhat(ytrai, dp[goct])
                dathem.append(ytrai)
                
                j+=1
            totnhat = laymax(yphai-1)
            if totnhat+1 > dp[chisogoc]:
                dp[chisogoc] = totnhat+1
        for y in dathem:
            xoabit(y)
        chiadetri(giua+1,phai)
    chiadetri(0,n-1)
    print(max(dp))