import sys
def F(x,y):
    n = x+1
    b= [0] *(n+2)
    p = [0] *(n+2)
    for m in range(1,n+1):
        b[m] = max(0,y+1-m)
        p[m] = p[m-1] + b[m]
    total = 0
    for s in range (1,x+1):
        h = s//2
        
        g = 2*(p[s-1]-p[h] )+b[s]
        if s % 2 == 0:
            g+= b[h] 
        total += (x+1-s) * g
    return total
def main():
    data = sys.stdin.read().split()
    
    t= int(data[0])
    out = []
    idx = 1
    for _ in range(t):
        x = int(data[idx]); y = int(data[idx+1]);idx+=2
        out.append(str(2*(F(x,y)+F(y,x))))
    print("\n".join(out))
main()