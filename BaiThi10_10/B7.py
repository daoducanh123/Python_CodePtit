class TheLoai:
    def __init__(self, id, ten):
        self.id = id
        self.ten = ten


class Phim:
    def __init__(self, id, theloai, ngay, ten, tap):
        self.id = id
        self.theloai = theloai
        self.ngay = ngay
        self.ten = ten
        self.tap = tap

    def __str__(self):
        return f"{self.id} {self.theloai.ten} {self.ngay} {self.ten} {self.tap}"


n, m = map(int, input().split())

theloai = {}
for i in range(1, n + 1):
    id = f"TL{i:03d}"
    ten = input().strip()
    theloai[id] = TheLoai(id, ten)

phim = []
for i in range(1, m + 1):
    ma_tl = input().strip()
    ngay = input().strip()
    ten = input().strip()
    tap = int(input())

    phim.append(Phim(f"P{i:03d}", theloai[ma_tl], ngay, ten, tap))


phim = sorted(phim, key=lambda x: (
    x.ngay[6:], x.ngay[3:5], x.ngay[:2],
    x.ten, -x.tap
))

for p in phim:
    print(p)