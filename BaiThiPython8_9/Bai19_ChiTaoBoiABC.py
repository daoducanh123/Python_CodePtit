n = int(input())

def sinh(s,n):
    if len(s) == n:
        a= s.count("A")
        b =s.count("B")
        c =s.count("C")
        
        if a > 0 and b > 0 and c > 0:
            if  a <= b and b <= c:
                print(s)
        return
    sinh(s+"A",n)
    sinh(s+"B", n)
    sinh(s+"C",n)
    
for length in range(3,n+1):
    sinh("",length)