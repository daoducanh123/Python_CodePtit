class HoaDon:
    def __init__ (self, id, name, cnt):
        self.id = id
        self.name= name
        self.cnt = cnt

# Tổng số tiền (được làm tròn ở dạng số nguyên)
        if cnt <= 50: self.total = round (100*cnt*1.02)
        
        elif cnt <= 100 : self.total = round((50*100 + (cnt-50)*150) * 1.03)
        else: self.total = round((50*100 + 50*150 + 200*(cnt-100)) * 1.05)
        
    def printt(self):
        print(self.id, self.name, self.total)
        
res = list()
t = int(input())
for i in range(t):
    id = f"KH{i+1:02d}"
    name = input()
    a = int(input())
    b = int(input())
    cnt = b - a

    hoaDon = HoaDon (id,name,cnt)
    res.append(hoaDon)
    
res = sorted(res,key=lambda x: x.total, reverse= True)
for i in res:
    i.printt()