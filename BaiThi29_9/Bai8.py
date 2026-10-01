import sys 
def main():
    data = sys.stdin.read().split()
    n,m,k = int (data[0]), int(data[1]), int(data[2])
    s= "".join(data[3:])

    team = [1 if ch == '1' else 0 for ch in s if ch in "01"][:n]
    w = [[0] * n for _ in range(m)]
    w [m-1] = [1-x for x in team]

    ones = [0] * n
    isb = [x == 1 for  x in team]
    for c in range(m-2,-1,-1):
        for p in range(n):
            ones[p] += w[c+1][p]
            if c + k + 1 <= m-1:
                ones[p] -= w[c+k+1][p]

        l= min(k,m-1-c)
        nxt = [ones[(p+1) % n] for p in range(n)]
        good = []
        for p in range(n):
            if isb[p]:
                good.append(nxt[p])
            else:
                good.append(l-nxt[p])
        w[c] = [team[p] if good[p] > 0 else 1 -team[p]
        for p in range(n)]
    print(" ".join(map(str,w[0])))
 

main()