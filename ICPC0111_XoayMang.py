import sys
input = sys.stdin.buffer.readline

T = int(input())
out = []

for _ in range(T):
    n, d = map(int, input().split())
    a = list(map(int, input().split()))

    d %= n

    out.append(' '.join(map(str, a[d:])))
    out[-1] += ' ' + ' '.join(map(str, a[:d]))

sys.stdout.write('\n'.join(out))