t = int (input())

def chk1(n):
    return (len(n) % 2 == 1)
def chk2(n):
    return (n[0] != n[1])
def chk3(n):
    for i in range(0, len(n)-2, 2):
        if n[i] != n[i+2]:
            return False
    return True
    

for _ in range(t):
    n  = input()

    if chk1(n) == True and chk2(n) == True and chk3(n) == True:
        print("YES")
    else: print("NO")    