#bai 1
diem = float(input())
if  0 <= diem and diem < 4:
    print("Điểm D")
elif 4 <= diem and diem < 6:
    print("Điểm C")
elif 6 <= diem and diem < 8.5:
    print("Điểm C")
elif diem >= 8.5:
    print("Điểm A")
    
#bai 2
cntChan = 0
cntLe = 0
arr = list (map(int, input().split()))
for a in arr:
    if a % 2 == 0:
        cntChan +=1 
    else:
        cntLe += 1
print(cntChan)
print(cntLe)
    