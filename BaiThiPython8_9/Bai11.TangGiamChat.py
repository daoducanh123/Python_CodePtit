t = int(input())

def Check(s):
    if len(s) < 3: return False

    # tim doan tang
    idx = 0
    while idx+1 <= len(s)-1 and s[idx] < s[idx+1]:
        idx+=1
    if idx == len(s)-1   or idx == 0:
        return False
    
    #tim doan giam
    while idx+1 <= len(s)-1 and s[idx] > s[idx+1]:
        idx+=1
    return idx == len(s)-1

# 3
# 12342 Y
# 23342 N
# 5678961 Y

while t > 0 :
    s = input()
    if Check(s):
        print("YES")
    else:
        print("NO")
    t -=1