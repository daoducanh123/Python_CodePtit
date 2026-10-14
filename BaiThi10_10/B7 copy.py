class BoPhim:
    def __init__(self, maPhim, tenPhim, ngayKhoiChieu, soTapPhim, theLoai):
        self.maPhim = maPhim
        self.tenPhim = tenPhim
        self.ngayKhoiChieu = ngayKhoiChieu
        self.soTapPhim = soTapPhim
        self.theLoai = theLoai

n,m = map(int,input().split())
dictTheLoai = dict()
for _ in range(n):
    maTheLoai = f"TL{_+1:03d}"
    theLoai = input()
    dictTheLoai[maTheLoai] = theLoai
    
listPhims = list()
for _ in range(m):
    maPhim = f"P{_+1:03d}"
    maTheLoai = input()
    ngayKhoiChieu = input()
    tenPhim = input()
    soTapPhim = int(input())
    boPhim = BoPhim(maPhim,tenPhim,ngayKhoiChieu,soTapPhim,dictTheLoai[maTheLoai])
    listPhims.append(boPhim)

#  thứ tự ưu tiên ngày khởi chiếu tăng dần, tên phim sắp xếp theo thứ tự từ điển, số tập phim giảm dần.
listPhims = sorted(listPhims, key=lambda x: x.soTapPhim, reverse=True)
listPhims = sorted(listPhims, key=lambda x: x.tenPhim)
# 31/01/2006
listPhims = sorted(listPhims, key=lambda x: (int(x.ngayKhoiChieu.split("/")[2]), int(x.ngayKhoiChieu.split("/")[1]), int(x.ngayKhoiChieu.split("/")[0])))

for i in range(len(listPhims)):
    boPhim = listPhims[i] 
    print(f"{boPhim.maPhim} {boPhim.theLoai} {boPhim.ngayKhoiChieu} {boPhim.tenPhim} {boPhim.soTapPhim}")