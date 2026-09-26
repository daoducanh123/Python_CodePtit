def demchuso(n):
    dem = [0] * 10
    if n <= 0:
        return dem
    
    heso =1
    while heso <= n:
        duoi = n - (n // heso)* heso
        chusohientai = (n//heso) % 10
        dau = n // (heso *10)
        
        if dau > 0:
            dem[0] += (dau-1) * heso+ (heso if chusohientai > 0 else duoi + 1) 
            
            
        for d in range(1,10):
            if d < chusohientai:
                dem[d] += (dau+1)*heso
            elif d == chusohientai:
                dem[d] += dau * heso + duoi + 1 
            else:
                dem[d] += dau * heso
        heso *= 10
        
    return dem

t = int (input())

for _ in range(t):
    a,b = map(int, input().split())
    if a > b:
        a,b = b,a
    demb = demchuso(b)
    dema = demchuso(a-1)
    
    ketqua = []
    for d in range(10):
        ketqua.append(demb[d] - dema[d])
        
    print(*ketqua)