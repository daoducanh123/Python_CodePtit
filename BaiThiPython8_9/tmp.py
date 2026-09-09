s = input()
# binary -> 8     001 010
while len(s) % 3 != 0:
    s = "0" + s
    
for i in range (0, len(s), 3):
    stringGroup = s[i:i+3]
    print(int(stringGroup,2),end=" ")