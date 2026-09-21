
    
import math
from itertools import permutations  
t = int(input())
for _ in range (t):
    n = int(input())
    a = [] 
    for i in range(n,0,-1):
        a.append(i) 
        
    for p in permutations(a):
       p = map(str,p)
       res = "".join(p)
       print (res)