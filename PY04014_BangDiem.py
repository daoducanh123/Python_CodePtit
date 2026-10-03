class HocSinh:
    cnt = 1
    def __init__(self, name, arrGpa, avg):
        self.msv = f"HS{HocSinh.cnt:02d}"
        self.name = name
        self.arrGpa = arrGpa
        self.avg = avg
        
        if avg >= 9:
            self.rank = "XUAT SAC"
        elif avg >= 8:
            self.rank = "GIOI"
        elif avg >= 7:
            self.rank = "KHA"
        elif avg >= 5:
            self.rank = "TB"
        else:
            self.rank = "YEU"

soHocSinh = int(input())
arrHocSinh = []

for _  in range(soHocSinh):
    name = input()
    sum = 0
    arrGpa =list(map(float, input().split()))
    
    sum = (arrGpa[0] + arrGpa[1]) * 2
    for i in range(2, 10):
        sum += arrGpa[i]
    avg = round(sum / 12+0.0001 , 1)
     
    hocSinh = HocSinh(name, arrGpa, avg)
    HocSinh.cnt += 1
    
    arrHocSinh.append(hocSinh)

    
# arrHocSinh = sorted(arrHocSinh, key = lambda x: x.avg, reverse=True) # theo gpa
arrHocSinh.sort(key=lambda x: x.msv)
arrHocSinh.sort(key=lambda x: x.avg, reverse = True)
for i in range(len(arrHocSinh)):
    print(f"{arrHocSinh[i].msv} {arrHocSinh[i].name} {arrHocSinh[i].avg:.1f} {arrHocSinh[i].rank}") # lamf tron 7.65 -> 7.7

    