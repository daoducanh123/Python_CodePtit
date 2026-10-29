# (a+bi)(c+di)=(ac-bd)+(ad+bc)i
class SoPhuc:
    def __init__(self, thuc, ao):
        self.thuc = thuc
        self.ao = ao
        self.am = False
        if ao < 0:
            self.am = True
            
    def Cong(self, other):
        t = self.thuc + other.thuc
        a = self.ao + other.ao
        return SoPhuc(t,a)
    def Nhan(self, other):
        t = self.thuc * other.thuc - self.ao * other.ao
        a = self.thuc * other.ao + self.ao * other.thuc
        return SoPhuc(t,a)
t = int (input())
for _ in range(t):
    a,b,c,d  = map(int,input().split())
    A = SoPhuc(a,b)
    B = SoPhuc(c,d)
    
    sophucTong = A.Cong(B)
    C = sophucTong.Nhan(A)        
    D = sophucTong.Nhan(sophucTong)
    
    if (C.am == False):
        print(f"{C.thuc} + {C.ao}i", end = ", ")
    else:
        print(f"{C.thuc} - {C.ao*-1}i", end = ", ")
    if (D.am == False):
        print(f"{D.thuc} + {D.ao}i")
    else:
        print(f"{D.thuc} - {D.ao*-1}i")