
class NhanVien:
    cnt = 0

    def __init__(self, name, d1, d2):
        self.name = name
        self.d1 = d1
        self.d2 = d2
        self.dtb = (d1 + d2) / 2
        self.msv = f"TS{NhanVien.cnt:02d}"
        self.rank = ""

    def CanNhac(self):
        if self.dtb < 5:
            self.rank = "TRUOT"
        elif self.dtb < 8:
            self.rank = "CAN NHAC"
        elif self.dtb <= 9.5:
            self.rank = "DAT"
        else:
            self.rank = "XUAT SAC"


n = int(input())
listNhanVien = []

for _ in range(n):
    name = input()
    d1 = float(input())
    d2 = float(input())

    if d1 >= 11:
        d1 /= 10
    if d2 >= 11:
        d2 /= 10

    NhanVien.cnt += 1
    nvien = NhanVien(name, d1, d2)
    nvien.CanNhac()
    listNhanVien.append(nvien)

listNhanVien.sort(key=lambda x: x.dtb, reverse=True)

for nvien in listNhanVien:
    print(f"{nvien.msv} {nvien.name} {nvien.dtb:.2f} {nvien.rank}")
