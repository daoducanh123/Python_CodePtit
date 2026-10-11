class SinhVien:
    cnt = 0
    def __init__(self, name, dtb,msv):
        self.name = name
        self.dtb = dtb
        self.msv = msv
        self.rank = ""
        
    def Rank(self):
        if self.dtb < 5:
            self.rank = "YEU"
        elif self.dtb >= 5 and self.dtb <= 6.9:
            self.rank = "TB"
        elif self.dtb >= 7 and self.dtb <= 7.9:
            self.rank = "KHA"
        elif self.dtb >= 8 and self.dtb <=  8.9:
            self.rank = "GIOI"
        elif self.dtb >= 9:
            self.rank = "XUAT SAC"    

n = int(input())
listSV = list()
for _ in range(n):
    # name
    name = input()
    # dtb
    arr = list(map(float,input().split()))
    sum = (arr[0] + arr[1])*2
    for _ in range (2, len(arr)):
        sum += arr[_]
    dtb = round ((sum/12)+0.01,1)
    
    #cnt
    SinhVien.cnt += 1
    #msv
    msv = f"HS{SinhVien.cnt:02d}"
    
    
    
    sinhvien = SinhVien(name, dtb,msv)
    sinhvien.Rank()
    listSV.append(sinhvien)

#sort
listSV = sorted(listSV, key=lambda x: x.dtb, reverse=True)

for i in range(len(listSV)):
    print(f"{listSV[i].msv} {listSV[i].name} {listSV[i].dtb:.1f} {listSV[i].rank}")