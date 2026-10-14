monThi = dict()
with open ("MONTHI.in", "r") as f:
    soMon = int(f.readline())
    for _ in range(soMon):
        maMonThi = f.readline().strip()
        tenMonThi = f.readline().strip()
        monThi[maMonThi] = tenMonThi

caThi = dict()
with open ("CATHI.in", "r") as f:   
    soCa = int(f.readline())
    maCa = ""
    for _ in range (soCa):
        maCa = f"C{_:03d}"
        ngayThi = f.readline().strip()
        gioThi = f.readline().strip()
        phongThi = f.readline().strip()
        caThi[maCa] = (ngayThi,gioThi,phongThi)

lichThi = list()
with open ("LICHTHI.in", "r") as f:
    soLichThi = int(f.readline())
    for _ in range(soLichThi):
        maCa = f.readline().strip()
        maMonThi = f.readline().strip()
        nhomThi = f.readline().strip()
        soLuongSinhVien = f.readline().strip()
        lichThi.append((maCa,maMonThi,nhomThi,soLuongSinhVien))

#  lịch thi theo thứ tự ngày, giờ và mã ca thi tăng dần.
# x[0] = maca
    # Ưu tiên 3: mã ca tăng dần
lichThi.sort(key=lambda x: x[0])

# Ưu tiên 2: giờ thi tăng dần
lichThi.sort(key=lambda x: caThi[x[0]][1])

# Ưu tiên 1: ngày thi tăng dần
lichThi.sort(key=lambda x: (
    int(caThi[x[0]][0].split("/")[2]),
    int(caThi[x[0]][0].split("/")[1]),
    int(caThi[x[0]][0].split("/")[0])
))
for maca, mamon, nhom, soSv in lichthi:
    ngaythi, giothi, phongthi = cathi[maca]
    tenmon = monthi[mamon]

    print(ngaythi, giothi, phongthi, tenmon, nhom, soSv)    

 
    
