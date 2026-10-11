class Phim: 
    cntMa = 0
    cntTheloai = 0
    
    def __init__(self,ma,name,date,sotap,theloai):
        self.ma = ma
        self.name=name
        self.date = date
        self.sotap =sotap
        self.theloai = theloai

#main
arr = list(map(int,input().split()))
cntTheloai = arr[0]
cntBoPhim = arr[1]

