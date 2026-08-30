class PhanSo:
    def __init__(self,tu,mau):
        self.tu = tu
        self.mau = mau


    def Output (self):
        print(f"{self.tu:.0f}/{self.mau:.0f}")

    def Rutgon (self):
        gcd = UCLN(self.tu, self.mau)
        self.tu //= gcd
        self.mau //= gcd

    def sum (self, p2):
        sumTu = self.tu * p2.mau + p2.tu * self.mau
        sumMau = self.mau * p2.mau
        tong = PhanSo(sumTu, sumMau)
        tong.Rutgon()

        print(f"{tong.tu}/{tong.mau}")
        

def UCLN(a,b):
    while b > 0:
        tmp = a
        a = b
        b = tmp % a
    return a


arr = input().split()
p1 = PhanSo(int(arr[0]), int(arr[1]))
p2 = PhanSo(int(arr[0]), int(arr[1]))


p1.sum(p2)

