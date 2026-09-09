def lanto(n):
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        
    return True
t = int(input())

for _ in range (t):
    s = input().strip()
    if not lanto(len(s)):
        print("NO")
        continue
    dem = 0
    
    for x in s:
        if x in "2357":
            dem +=1
    if dem > len(s) -dem:
        print("YES")
        
    else:
        print("NO")