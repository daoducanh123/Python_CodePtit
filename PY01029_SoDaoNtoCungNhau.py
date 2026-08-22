def ucln(a,b):
    while b!= 0:
        tmp = a
        a = b
        b = tmp % a
    return a


def rev(n):
    rev_num = 0
    while n > 0:
        
        rev_num = rev_num* 10 + n%10
        n //= 10

    return rev_num


# main
test = int(input())
for t in range (0, test):
    n = int(input())

    rev_num = rev(n)
    if ucln(n, rev_num) != 1:
        print("NO")
    else:
        print("YES")
