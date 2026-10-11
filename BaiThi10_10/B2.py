class HoaDon:
    def __init__ (self, id, name, cnt):
        self.id = id
        self.name= name
        self.cnt = cnt

        if cnt <= 50: self.total = round (100*cnt*1.02)
        
        elif cnt <= 100 : self.total = round((5000+(cnt-50)*150)*1.03)
        else: self.total = round((5000+50*150+200*(cnt-100))*1.05)
        
    def printt(self):
        print(self.id, self.name, self.total)
        
z= []
for _ in range(int(input())):
    s = input()
    a = int(input())
    b = int(input())
    cnt = b -a
    id = f"KH{_+1:02d}"
    e = HoaDon (id,s,cnt)
    z.append(e)
    
z = sorted(z,key=lambda x: -x.total)
for i in z:
    i.printt()