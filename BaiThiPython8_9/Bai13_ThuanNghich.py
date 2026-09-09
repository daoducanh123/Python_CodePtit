# def check(n):
#     s = str(n)
#     if len(s) % 2 ==0:
#         return False
#     if s != s[::-1]:
#         return False
#     for c in s:
#         if int(c) %  2 != 0:
#             return False
#     return True

# t = int(input())
# while t > 0:
#     n = int(input())
#     for i in range(22,n , 2):
#         if check(i):
#             print(i, end =  " ")
    
#     print()
#     t-=1


t = int(input())
arr = []

def check(s):
    for ss in s:
        if ss not in "02468":
            return False
    return True

for i in range (1,1000): 
    s = str(i)
    if check(s) == False:
        continue
    s = s + s[::-1] # 123321
    arr.append(s)
        
for _ in range(t):
    n = int(input())
    for i in range (len(arr)):
        num = int(arr[i])
        if int(arr[i]) >= n:
            break
        else:
            print(num,end=" ")
    print()            
