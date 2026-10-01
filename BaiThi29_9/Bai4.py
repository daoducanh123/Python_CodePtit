import sys 
from collections import deque

def main():
    s = "".join(sys.stdin.read().split())
    bits = [c for c in s if c in "01"]
    def parse(part):
        mask = 0
        for p in range(16):
            if part[p] == '1':
                mask |= 1 << p
        return mask

    start = parse(bits[:16])
    end = parse(bits[16:32])

    prev = {start:None}
    q = deque([start])

    dirs = ((1,0), (-1,0), (0,1), (0,-1))

    while q:
        cur = q.popleft()
        if cur == end:
            break
        for p in range(16):
            if (cur >> p) &1:
                i,j = divmod(p,4)
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < 4 and 0 <= nj < 4:
                        t = ni* 4 + nj
                        if not(cur >> t) & 1:
                            nxt = cur ^ (1<<p) ^ (1<<t)
                            if nxt not in prev:
                                prev[nxt] = (cur,p,t)
                                q.append(nxt)
    path = []
    cur = end
    while prev[cur] is not None:
        par,p,t = prev[cur]
        path.append((p // 4 + 1,p % 4 + 1, t //4+ 1, t%4+1))
        cur = par
    path.reverse()

    out = [str(len(path))]
    for u,v,x,y in path:
        out.append(f"{u} {v} {x} {y}")
    print("\n".join(out))

main()