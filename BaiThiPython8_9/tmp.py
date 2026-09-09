s1 = input()
s2 = input()

arr1 = s1.lower().split(" ")
arr2 = s2.lower().split(" ")

set1 = set(arr1)
set2 = set(arr2)

d = dict()
for x in set1:
    if x not in d:
        d[x] = 1
    else:
        d[x] += 1 
for x in set2:
    if x not in d:
        d[x] = 1
    else:
        d[x] += 1 

dSorted = dict(sorted(d.items()))
# hop    
for key, value in dSorted.items():
    if value >= 1:
        print(key, end = " ")
print()
# giao
for key, value in dSorted.items():
    if value > 1:
        print(key, end = " ")   