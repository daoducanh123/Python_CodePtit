
def Chk(s):
    sum = 0
    for i in range ((len(s))):
        x = int (s[i])
        sum += x
    res = str(sum)
    if len(res) <= 1:
        return False
    return res == res[::-1]
    

t = int(input())
for _ in range (t):
    s = input()
    if (Chk(s)):
        print("YES")
    else:
        print("NO")