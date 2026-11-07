n,m = map(int, input().split())
arr = list(map(int,input().split()))
brr = list(map(int,input().split()))
a= set(arr)
b= set(brr)

# giao
giao = a & b

s1 = a-b
s2 = b-a
print(*sorted(giao))
print(*sorted(s1))
print(*sorted(s2))


# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
# brr = list(map(int, input().split()))

# # Giao A và B
# giao = []
# for x in arr:
#     if x in brr and x not in giao:
#         giao.append(x)

# # Hiệu A - B
# s1 = []
# for x in arr:
#     if x not in brr and x not in s1:
#         s1.append(x)

# # Hiệu B - A
# s2 = []
# for x in brr:
#     if x not in arr and x not in s2:
#         s2.append(x)

# print(*giao)
# print(*s1)
# print(*s2)