import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    t = int(input_data[0])
    idx = 1
    for _ in range(t):
        n = int(input_data[idx])
        idx+=1
        
        
        segments = []
        for _ in range(n):
            x1 = int(input_data[idx])
            x2 = int(input_data[idx+1])
            segments.append((x1,x2))
            idx+=2
            
        segments.sort(key=lambda seg: seg[1])
        count = 0
        lastend= -1
        for start, end in segments:
            if start>= lastend:
                count+=1
                lastend = end
                
        print(count)
        
if __name__ == '__main__':
    solve()