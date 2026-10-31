# Nhập thêm một giá trị K gọi là ngưỡng cân đối của ma trận.  Trong trường hợp độ chênh lệch không quá K thì ma trận được coi là cân đối, nếu lớn hơn K thì không cân đối.

n = int(input())
arr = list()
for i in range(n):
    row = list(map(int,input().split()))
    arr.append(row)
k = int(input())
    
cntTren = 0
cntDuoi  = 0
for i in range(0,n):
    for j in range(0,n):
        if i + j == n-1:
            continue
        else:
            if i + j > n-1:
                cntDuoi += arr[i][j]
            else:                           
                cntTren +=arr[i][j]
                
                
if abs(cntTren-cntDuoi) > k:
    print("NO")
else:
    print("YES")
print (abs(cntTren-cntDuoi))