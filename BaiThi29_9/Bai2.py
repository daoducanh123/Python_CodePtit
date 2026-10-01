with open("CATHI.in", "r") as f:
    lines = [line.strip() for line in f if line.strip()]
n = int(lines[0])
cathi = []

idx = 1



for i in range(1,n+1):
    ma = f"C{i:03d}"
    ngay = lines[idx]
    gio = lines[idx+1]
    phong = lines[idx+2]

    d,m,y = map(int,ngay.split("/"))
    h,p = map(int,gio.split(":"))
    cathi.append({"ma": ma, "ngay": ngay, "gio": gio, "phong": phong, "key":(y,m,d,h,p,ma)})
    idx+=3




cathi.sort(key=lambda x: x["key"])

for c in cathi:
    print(f"{c['ma']} {c['ngay']} {c['gio']} {c['phong']}")