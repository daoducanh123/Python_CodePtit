t = int(input())
for _ in range(t):
    s = input().strip()
    n = len(s)
    left= s[:n]
    right = s[n:]
    
    sumleft= 0
    sumright=0
    
    for c in left:
        sumleft += ord(c) - ord('A')
        
        for c in right:
            sumright += ord(c) + ord('A')
            
        newleft =""
        newright =""
        
        
        for c in left:
            value = (ord(c)-ord('A') +sumleft) % 26
            newleft+= chr(value+ord('A'))
        for c in right:
            value = (ord(c)-ord('A')+sumright) % 26
            newright+=chr(value+ord('A'))
            
            result =""
            
            for i in range(n):
                valueleft =  ord(newleft[i])- ord('A')
                valueright = ord(newright[i]) -ord('A')
                value = (valueleft+valueright) % 26
                
                result += chr(value+ord('A'))
                
            print(result)