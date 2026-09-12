def Tong(s):
    res = 0
    for i in range (len(s)):
        res += int(s[i])
    return res

n = int(input())
if n < 0:
    n = abs(n)
s = str(n)
cnt = 0
while(len(s) > 1):
    tong = Tong(s)
    cnt += 1
    s = str(tong)
print(cnt)