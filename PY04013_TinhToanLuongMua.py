
n = int(input())
d = dict()
listTram = list()

for _ in range(n):
    cnt = _ + 1
    name = input()
    #ma T01
    ma = f"T{cnt:02d}"

    #Dong Anh
    # 07:30
    # 08:00
    # 60 60

    vao = input().split(":")
    ra = input().split(":")
    luongmua1h = float(input())

    # doi
    hvao = int(vao[0]) * 60 + int(vao[1])
    hra = int(ra[0]) * 60 + int(ra[1])
    tgian_phut = abs(hra - hvao)

    # cho vao dict
    if name in d:
        d[name] = (d[name][0],
                   d[name][1] + luongmua1h,
                   d[name][2] + tgian_phut)
    else:
        ma = f"T{len(d) + 1:02d}"
        d[name] = (ma, luongmua1h, tgian_phut)

for dd in d:
    luongmua = d[dd][1] * 60 / d[dd][2]
    print(f"{d[dd][0]} {dd} {luongmua:.2f}")
