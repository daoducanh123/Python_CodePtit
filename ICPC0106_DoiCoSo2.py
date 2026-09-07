

# 2
# 8
# 10010100010010101
# 2
# 10010100010010101


stringHex = "0123456789ABCDEF"
t = int (input())
while t > 0:
        
    b = int (input())
    s = input()
    c = 0
    match b:
        case 2:
            c = 1   
        case 4:
            c = 2
        case 8:
            c = 3
        case 16:
            c = 4

    # 00 0011 -> len(s) = 6
    # c = 4 -> 6 % 4 == 2
    # Đếm số bit cần vá
    padNum = 0
    if len(s) % c != 0:
        padNum = c-(len(s) % c)

    # Vá
    stringRes = ""
    stringPadding = ""
    for i in range (0,padNum):
        stringPadding = stringPadding + "0"
    stringRes = stringPadding + s

    #Group đổi lần lượt    
    # 0000 0011 -> 3
    for i in range (0, len(stringRes), c):
        stringGroup = int(stringRes[i:i+c],2)
        if b == 16:
            stringGroup = stringHex[stringGroup]
        print(stringGroup, end = "")
    print()
    
    t-=1    


        