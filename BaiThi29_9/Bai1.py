monhoc = {}
with open ("MONTHI.in", "r") as f:
    n = int(f.readline())
    for _ in range (n):
        mamon = f.readline().strip()
        tenmon = f.readline().strip()
        f.readline()
        monhoc[mamon] = tenmon

cathi = {}
with open ("CATHI.in", "r") as f:
    n = int(f.readline())
    for i in range(1,n+1):
        ngay = f.readline().strip()
        gio = f.readline().strip()
        phong = f.readline().strip()

        maca = f"C{i:03d}"
        cathi[maca] = (ngay,gio,phong)

lichthi = []
with open ("LICHTHI.in","r")as f:
    n = int(f.readline())
    for _ in range(n):
        maca, mamon, nhom, sosv = f.readline().split()
        lichthi.append((maca,mamon,nhom,sosv))

def key(x):
    maca = x[0]
    ngay,gio,phong = cathi[maca]
    d,m,y = map(int,ngay.split("/"))
    h,p = map (int,gio.split(":"))


    return (y,m,d,h,p,maca)
lichthi.sort(key=key)
for maca, mamon,nhom,sosv in lichthi:
    ngay,gio,phong = cathi[maca]
    print(ngay,gio,phong,monhoc[mamon],nhom,sosv)