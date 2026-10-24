
# s = input()
# a = [0] * len(s)
# visited = [False] * len(s)

# def Try(pos):
#     for j in range(0, len(s)):
#         if not visited[j]:
#             visited[j] = True
#             a[pos] = j
#             if pos == len(s)-1:
#                 for aa in a:
#                     print(s[aa], end ="")
#                 print()
#             else:
#                 Try(pos+1)
#             visited[j] = False

# Try(0)

from itertools import permutations

s = input()

# Tạo tất cả các hoán vị của chuỗi s
ds = permutations(s) # ds: là một iterator (đối tượng cho phép duyệt lần lượt các kết quả), không phải tuple hay list.
# ds = sorted(permutations(s), reverse=True) # bonus
# Duyệt qua từng hoán vị
for x in ds: # mỗi x = ('a', 'b', 'c')
    # Ghép các ký tự thành một chuỗi rồi in ra
    print(''.join(x))