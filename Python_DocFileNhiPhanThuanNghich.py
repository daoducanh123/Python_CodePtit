import pickle

with open ("DATA1.in", "rb") as file1:
    f1= pickle.load(file1)
with open ("DATA2.in", "rb") as file2:
    f2= pickle.load(file2)
    
d = dict()

#so lan xuat hien trong file 1 va 2
for x in f1:
    if x in d:
        d[x] += 1
    else:
        d[x] = 1
for x in f2:
    if x in d:
        d[x] += 1
    else:
        d[x] = 1
res = list()
for x in d:
    ok = True
    s = str(x)
    # xuat hien trong 2 file
    if x not in f1 or x not in f2:
        continue
    # thuan nghich
    if s != s[::-1]:
        continue
    # full le
    for i in range(len(s)):
        num = int (s[i])
        if (num % 2 == 0):
            ok = False
            break
    if not ok:
        continue
    
    # len = ler vaf != 1
    if len(s) % 2 == 0 or len(s) == 1:
        continue
    
    # luu kqua
    res.append(x)
    res = sorted(res)
    
for x in res[:10]: # in toi da 10 thangwf && ko so bi rte 
    cnt = d[x]
    print(x, cnt)