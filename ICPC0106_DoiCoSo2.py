

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
    
    while len(s) % c != 0:
        s = "0" + s

    #Group đổi lần lượt    
    # 0000 0011 -> 3
    for i in range (0, len(s), c):
        stringGroup = int(s[i:i+c],2)
        if b == 16:
            stringGroup = stringHex[stringGroup]
        print(stringGroup, end = "")
    print()
    
    t-=1    


        