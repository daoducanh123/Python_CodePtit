class SinhVien:
    def __init__(self, maSinhVien, hoTen, lop):
        self.maSinhVien = maSinhVien
        self.hoTen = hoTen
        self.lop = lop
        self.diem = 10
        
n = int(input())
listSinhVien = list()
for _ in range(n):
    maSinhVien = input()
    hoTen = input()
    lop = input()
    sinhVien = SinhVien(maSinhVien,hoTen,lop)
    listSinhVien.append(sinhVien)
    
for _ in range(n):
    listInput = input().split()
    ma = listInput[0]
    diemDanh = listInput[1]
    
    for sv in listSinhVien:
        if sv.maSinhVien==ma: # dungf == hay equals??
            for d in diemDanh:
                if d == 'm': # d == "m" hay d == 'm'
                    sv.diem -= 1
                elif d == 'v':
                    sv.diem -= 2
            if sv.diem < 0:
                sv.diem = 0
            break
for sv in listSinhVien:
    print (f"{sv.maSinhVien} {sv.hoTen} {sv.lop} {sv.diem} ", end = "")
    if sv.diem == 0:
        print("KDDK", end= "")
    print()