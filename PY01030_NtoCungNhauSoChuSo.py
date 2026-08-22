
def ucln(a,b):
    while b!=0:
        tmp = a
        a = b
        b = tmp % a 

    return a

n,k = map(int,input().split())


start = 10**(k-1)
end = 10 **(k)-1


cnt = 0
for i in range (start, end+1, 1):
    if cnt == 10:
        print()
        cnt = 0
    if ucln(i,n) == 1:
        print(i,end = " ")
        cnt += 1
    else:
        continue