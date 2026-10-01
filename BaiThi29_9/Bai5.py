import sys
from collections import deque

def main():
    data= sys.stdin.buffer.read().split()
    pos = 0

    t = int(data[pos]); pos += 1
    M = 1<<32
    out = []
    for _ in range(t):
        xa,ya,xb,yb = (int(v) for v in data[pos:pos+4]); pos+=4
        n = int(data[pos]);pos+=1
        cells = set()
        for _ in range(n):
            x = int (data[pos]); y1 = int(data[pos+1]); y2 = int(data[pos+2]); pos+=3
            base = (x+1)*M + 1
            for y in range(y1,y2+1):
                cells.add(base+y)
        s= (xa+1)*M+ya+1
        e= (xb+1)*M+yb+1

        if s not in cells or e not in cells:
            out.append("-1")
            continue
        dist = {s:0}
        q=  deque([s])
        offs= (M - 1, M, M+1,-1, 1, -M-1,-M,-M+1)
        ans = -1
        while q:
            cur = q.popleft()
            if cur == e:
                ans = dist[cur]
                break
            d= dist[cur] + 1
            for o in offs:
                nx = cur+o
                if nx in cells and nx not in dist:
                    dist[nx]=d
                    q.append(nx)
        out.append(str(ans))

    print("\n".join(out))
main()