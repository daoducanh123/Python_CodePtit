class SinhVien:
    cnt = 0
    def __init__(self, thutu,name, ma, diemTinHoc, diemChuyenMon):
        self.thutu = thutu
        self.name= name
        self.ma = ma
        self.diemTinHoc = diemTinHoc
        self.diemChuyenMon = diemChuyenMon
        
        self.tongDiem = 0.0
        self.mon = ""
        self.rank = ""
        
    def Ma (self):
        if ma[0] == 'A':
            self.mon = "TOAN"
        elif ma[0] == 'B':
            self.mon = "LY"
        elif ma[0] == 'C':
            self.mon = "HOA"
        if ma[1] == '1':
            self.tongDiem+=2.0
        elif ma[1] == '2':
            self.tongDiem+=1.5
        elif ma[1] == '3':
            self.tongDiem+=1.0
    def Rank(self):
        if self.tongDiem<18:
            self.rank ="LOAI"
        else:
            self.rank ="TRUNG TUYEN"
        

n = int (input())
listSinhVien =  list()
for _ in range (n):
    thutu = f"GV{_+1:02d}"
    name = input()
    ma = input()
    diemTinHoc = float(input())
    diemChuyenMon = float(input())
    sinhVien = SinhVien(thutu, name, ma , diemTinHoc , diemChuyenMon)
    sinhVien.Ma()
    sinhVien.tongDiem += sinhVien.diemChuyenMon + sinhVien.diemTinHoc*2
    sinhVien.Rank()
    listSinhVien.append(sinhVien)
listSinhVien= sorted(listSinhVien, key = lambda x: -x.tongDiem)    
for sinhVien in listSinhVien:
    print(f"{sinhVien.thutu} {sinhVien.name} {sinhVien.mon} {sinhVien.tongDiem:.1f} {sinhVien.rank}")
    