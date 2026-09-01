t = int(input())
while t>0:
    xau = input()
    idx = 0
    res = 100000000000000000

    while idx < len(xau):
        num = 0
        isNum = False
        while idx < len(xau) and xau[idx].isdigit() == True:
            num = num * 10 + int(xau[idx])    
            idx+=1
            isNum = True
        
        if isNum == True:
            res = min(num,res)
        else:
            idx += 1
            # 0
            # num = 1
            # 123abc23
            #nho chk thop cuoi
    print(res)
    t-=1