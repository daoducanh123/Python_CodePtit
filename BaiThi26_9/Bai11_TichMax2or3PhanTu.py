n = int(input())
a = list(map(int,input().split()))
a.sort()


p1 = a[0]*a[1]

p2 = a[n-2]*a[n-1]
p3 = a[0] * a[1] * a[n-1]
p4 = a[n-3]*a[n-2]*a[n-1]

print(max(p1,p2,p3,p4))