


t = int(input())
for _ in range(t):
    s = list(input().strip())
    n = len(s)
    found  = False
    for i in range(n-2,-1,-1):
        best = -1
        pos = -1
        for j in range(i+1,n):
            if i == 0 and s[j] == '0':
                continue
            if s[j] < s[i]:
                if best == -1 or s[j] > best:
                    best = s[j]
                    pos = j
        if pos != -1:
            for j in range(i+1,n):
                if s[j] == best:
                    pos = j
                    break
            s[i] , s[pos] = s[pos] , s[i]
            print("".join(s))
            found = True
            break
    if not found:
        print(-1)