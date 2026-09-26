def languyento(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

while True:
    try:
        n = int(input())
        a = list(map(int,input().split()))
    except:
        break
    
    
    b = []
    
    for x in  a:
        if x not in b:
            b.append(x)
            
    m = len(b)
    tongtoanbo = sum(b)
    tongtrai = 0 
    timthay = False
    
    for i in range(m-1):
        tongtrai += b[i]
        tongphai = tongtoanbo -tongtrai
        if languyento(tongtrai) and languyento(tongphai):
            print(i)
            timthay= True
            break
        
    if not timthay:
        print("NOT FOUND")