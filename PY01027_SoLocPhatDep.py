s = input()

idx = 0
ok = True
# 6686882
while idx < len(s):
    if s[idx:idx+3] == "688":
        idx+=3
    elif s[idx:idx+2] == "68":
        idx += 2
    elif s[idx] == "6":
        idx += 1
    else:
        ok = False
        break
if ok:
    print("YES")
else:
    print("NO")