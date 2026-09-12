    # 001 010
    # 11001100
    
s = input()
while len(s) % 3 != 0:
    s = "0" + s
    
while len(s) > 0:
    stringGroup = s[0:3]
    print(int(stringGroup,2), end = "")
    s = s[3:]