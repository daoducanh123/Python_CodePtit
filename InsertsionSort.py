n = int(input())
arr = list(map(int, input().split()))

# 4
# 5 3 2 4
# i j
#   min = 3 
#   
# selection
# for i in range (0, len(arr)-1):
#     pos = i
#     for j in range (i+1, len(arr)):
#         if (arr[j] < arr[pos]):
#             pos = j
#     # swap
#     tmp = arr[i]
#     arr[i] = arr[pos]
#     arr[pos] = tmp

# print(arr)

#insertion sort

# 4 
# 3 7 5 2
# for i in range (0, len(arr)):
#     value = arr[i]
#     j = i -1
#     while j >= 0 and arr[j] > value:
#         arr[j+1] = arr[j]
#         j-=1
#     arr[j+1] = value
    
# print(arr)

# doi cho truc tiep
for i in range (0, len(arr)-1):
    for j in range (i + 1, len(arr)):
        #swap
        if (arr[j] < arr[i]):
            tmp = arr[i] 
            arr[i] = arr[j]
            arr[j] = tmp
print(arr) 

# noi bot
# 4
# 5 4 3 2

# i = 0 
# j j
# 4 5 3 2
#   j j
# 4 3 5 2
#     j j 
# 4 3 2 5
# j 
for i in range (0, len(arr)-1):
    for j in range (0, len(arr)-i-1):
        if arr[j+1] < arr[j]:
            tmp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = tmp
print(arr)