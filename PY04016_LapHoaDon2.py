from datetime import datetime

class Khach:
    def __init__(self, ma, name, soPhong, ngay, tien):
        self.ma = ma
        self.name = name
        self.soPhong = soPhong
        self.ngay = ngay
        self.tien = tien

listKhach = list()
n = int(input())

for i in range(n):
    ma = f"KH{(i+1):02d}"
    name = input()
    soPhong = input()
    ngayNhanString = input()
    ngayTraString = input()
    tienPhatSinh = int(input())

    ngayNhan = datetime.strptime(ngayNhanString.strip(), "%d/%m/%Y")
    ngayTra = datetime.strptime(ngayTraString.strip(), "%d/%m/%Y")
    ngay = (ngayTra - ngayNhan).days + 1

    # tinh tien
    tang = int(soPhong[0])  # 1: 25 2:34 3:50 4:80
    tienCuaTang = 0

    if tang == 1:
        tienCuaTang = 25
    elif tang == 2:
        tienCuaTang = 34
    elif tang == 3:
        tienCuaTang = 50
    elif tang == 4:
        tienCuaTang = 80

    tien = tienCuaTang * ngay + tienPhatSinh
    khach = Khach(ma, name, soPhong, ngay, tien)
    listKhach.append(khach)

listKhach = sorted(listKhach, key=lambda x: x.tien, reverse=True)

for l in listKhach:
    print(f"{l.ma} {l.name} {l.soPhong} {l.ngay} {l.tien}")