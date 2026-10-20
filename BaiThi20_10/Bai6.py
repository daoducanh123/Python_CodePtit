from collections import Counter
n,k = map(int,input().split())
a= list(map(int,input().split()))
cnt = Counter(a)
print(max(cnt.values())*2)