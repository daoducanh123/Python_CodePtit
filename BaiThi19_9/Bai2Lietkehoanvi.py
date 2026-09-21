import math
from itertools import permutations
t = int(input())
for _ in range(t):
    n = int(input())
    
    #in so luonng hoan vi
    print(math.factorial(n))
    #sinh hoan vi tu lon xuong
    a = list(range(n, 0, -1))
    
    for p in permutations(a):
        print(''.join(map(str,p)),end = ' ')
    print()
    
    
