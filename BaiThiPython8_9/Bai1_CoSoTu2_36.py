digits= "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

t = int(input())
for _ in range (t):
    n,b = map(int,input().split())
    result = ""
    while n >0:
        du = n % b
        result = digits[du] + result
        n= n//b
        
    print(result)