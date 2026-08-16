
def chkNto(num):
    if (num < 2): return False

    for x in range(2, int(num ** 0.5) + 1 ):
        if (num % x == 0):
            return False
    return True

def SumUCLN(num):
    strNum = str(num)
    sum = 0
    for s in strNum:
        sum += int(s)
    return chkNto(sum)

def UCLN(a,b):
    while b != 0:
        tmp = a
        a = b
        b = tmp % b
    return a

test = int(input())
while test > 0:
    a,b = map(int, input().split())
    if (SumUCLN(UCLN(a,b))):
        print("YES")
    else:
        print ("NO")

    test -= 1