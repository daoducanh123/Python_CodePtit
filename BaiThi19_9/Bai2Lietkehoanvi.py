
    
# import math
# from itertools import permutations  
# t = int(input())
# for _ in range (t):
#     n = int(input())
#     a = [] 
#     for i in range(n,0,-1):
#         a.append(i) 
        
#     for p in permutations(a):
#        p = map(str,p)
#        res = "".join(p)
#        print (res)
       
       
# 321

def Try ():
    for j in range (n,0,-1):
        if visited[j] == False:
            visited[j] = True
            a.append(j)
            if len(a) == n:
                for aa in a:
                    print (aa,end =  " ")
                print()
            else:
                Try()
            a.pop()
            visited[j] = False
            

#main
t = int(input())
for _ in range(t):
    n = int(input())
    visited = [False] * (n+1)
    a = []
    Try()