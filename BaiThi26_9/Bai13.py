n = int(input())

def prime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

s = str(n)[::-1]
m = len(s)

dp = {(0,0,0,0,0):1 }
for i in range(m):
    nd = int (s[i])
    newdp = {}
    
    for (carry,sx,sy,hx,hy), cnt in dp.items():
        for x_digit in range(10):
            for y_digit in range(10):
                total = x_digit + 2 * y_digit +carry
                if total % 10 != nd:
                    continue
                neewcarry = total//10
                
                key=(neewcarry,sx+x_digit,sy+y_digit,hx or (x_digit!=0),hy or (y_digit!=0))
                newdp[key] = newdp.get(key,0) + cnt
    dp = newdp
ans = 0

for (carry, sx, sy, hx,hy), cnt in dp.items():
    if carry == 0 and hx and hy and prime(sx) and prime(sy):
        ans+= cnt
        
print(ans)