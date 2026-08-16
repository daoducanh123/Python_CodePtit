str = input()
cntThuong = 0
cntHoa = 0

for s in str:
    if s.isalpha() and s.isupper():
        cntHoa += 1
    elif s.isalpha() and s.islower():
        cntThuong += 1
if cntThuong >= cntHoa:
    lowerStr = str.lower()
    print(lowerStr)
else:
    upperStr = str.upper()
    print(upperStr)
