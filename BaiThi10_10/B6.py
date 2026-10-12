# 2
# INT1155 -mamon
# Tin hoc co so 2 -monthi
# INT1339
# Ngon ngu lap trinh C++
monthi = dict()
with open ("MONTHI.in", "r") as f:
    n = int(f.readline()) # so luong monthi
    for _ in range(n):
        mamon = f.readline().strip()
        tenmon = f.readline().strip()
        monthi[mamon] = tenmon

# 3
# 25/10/2026
# 07:00
# 101
# 25/10/2026
# 13:30
# 102
# 26/10/2026
# 07:00
# 201
cathi = dict()
with open ("CATHI.in", "r") as f:
    n = int(f.readline())
    for i in range(n):
        maca = f"C{i:03d}" # C001 C002
        ngaythi = f.readline().strip()
        giothi = f.readline().strip()
        phongthi = f.readline().strip()

        cathi[maca] = (ngaythi,giothi,phongthi)

# 3
# C002 INT1339 01 120
# C001 INT1155 02 80
# C003 INT1155 01 100
lichthi = list() # Nhưng dict cũng sort được; ở bài này list tiện hơn vì mỗi lịch thi là một bộ dữ liệu cần giữ nguyên.
with open ("LICHTHI.in", "r") as f:
    n = int(f.readline())
    for i in range(n):
        inputString = f.readline().split()
        maca = inputString[0]
        mamon = inputString[1]
        nhom = inputString[2]
        soSv= inputString[3]

        lichthi.append((maca,mamon,nhom,soSv))

# sorted In danh sách lịch thi theo thứ tự ngày, giờ và mã ca thi tăng dần. Mỗi dòng gồm:

# `Ngày_thi Giờ_thi Phòng_thi Tên_môn_thi Nhóm_thi Số_sinh_viên`
# 25/10/2026 07:00 101 Tin hoc co so 2 02 80
# 25/10/2026 13:30 102 Ngon ngu lap trinh C++ 01 120
# 26/10/2026 07:00 201 Tin hoc co so 2 01 100
lichthi = sorted (lichthi, key = lambda x:(    # x = ('C002', 'INT1339', '01', '120')
            # x[0] = maca
            int(cathi[x[0]][0].split("/")[2]), # cathi[x[0]][0] = cathi[maca][0] = ngaythi = '25/10/2026' || .split("/")[2] -> năm
            int(cathi[x[0]][0].split("/")[1]), # thangs
            int(cathi[x[0]][0].split("/")[0]), # ngay

            cathi[x[0]][1],                     # gio (co the sort theo string luon)
            x[0]                    
        )
)

for maca, mamon, nhom, soSv in lichthi:
    ngaythi, giothi, phongthi = cathi[maca]
    tenmon = monthi[mamon]

    print(ngaythi, giothi, phongthi, tenmon, nhom, soSv)    
