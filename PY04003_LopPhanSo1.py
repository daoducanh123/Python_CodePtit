class PhanSo:
    def __init__(self,tu,mau):
        self.tu = tu
        self.mau = mau

    def Output (self):
        print(f"{self.tu:.0f}/{self.mau:.0f}")

    @staticmethod
    def Rutgon (p):
        gcd = UCLN(p.tu, p.mau)
        p.tu /= gcd
        p.mau /= gcd

def UCLN(a,b):
    while b > 0:
        tmp = a
        a = b
        b = tmp % a
    return a


# tu, mau = map(int, input().split())
arr = input().split()
tu = int(arr[0])
mau = int(arr[1])

p = PhanSo(tu,mau)
PhanSo.Rutgon(p)
p.Output()
