import sys
def main():
    w = list(map(int,sys.stdin.read().split()))[:12]
    best = [float('inf')]
    def go (rest,sums):
        if not rest:
            best[0] = min(best[0], max(sums)-min(sums))
            return
        first = rest[0]
        others = rest[1:]
        n = len(others)
        for i in range(n):
            for j in range(i+1,n):
                s = first + others[i] + others[j]
                nxt = [others[k] for k in range(n) if k !=i and k !=j]
                go (nxt,sums+[s])
    go(w, [])
    print(best[0])
main()