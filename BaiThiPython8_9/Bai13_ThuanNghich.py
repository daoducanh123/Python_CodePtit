def check(n):
    s = str(n)
    if len(s) % 2 ==0:
        return False
    if s != s[::-1]:
        return False
    for c in s:
        if int(c) %  2 != 0:
            return False
    return True

t = int(input())
while t > 0:
    n = int(input())
    for i in range(22,n , 2):
        if check(i):
            print(i, end =  " ")
    
    print()
    t-=1


# t = int(input())

# def check(s):
#     for i in range(0,len(s)):
#         if s[i] not in "02468":
#             return False
#         else:
#             return True
    
# while t > 0:
#     n = int(input())

#     # 0 -> 999
#     for i in range (1, 1000):
#         s = str(i)
#         if check(s):
#             sRev = s [::-1]
#             s = s + sRev
#             res = int(s)
#             if res< n:
#                 print(res, end = " ")
    
#     print()
#     t-=1