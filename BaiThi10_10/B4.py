import math
class Gamer:
    cnt = 0
    def __init__(self, ma, name, gio, phut):
        self.ma = ma
        self.name = name
        self.gio = gio
        self.phut = phut        
        
#main
listGamer = list()
n = int (input())
for _ in range(n):
    
    ma = input()
    name = input()
    stringTimeVao = input().split(":")
    stringTimeRa = input().split(":")
    
    gioVao = int(stringTimeVao[0])
    phutVao = int (stringTimeVao[1])
    gioRa = int(stringTimeRa[0])
    phutRa = int (stringTimeRa[1])
    
    resVao = gioVao * 60 + phutVao
    resRa = gioRa * 60 + phutRa
    res = abs(resRa - resVao)
    resGio = res // 60
    resPhut = res % 60
    
    
    
    # 1:00 60p
    # 2:30 150 
    # 150 - 60 = 90 
    
    # 90 / 60 = 1 du 30
    
    
    
    gamer = Gamer(ma,name,resGio,resPhut)
    listGamer.append(gamer)
listGamer = sorted(listGamer, key = lambda x: x.phut,reverse= True)
listGamer = sorted(listGamer, key = lambda x: x.gio,reverse= True)

for i in range(len(listGamer)):
    print(f"{listGamer[i].ma} {listGamer[i].name} {listGamer[i].gio} gio {listGamer[i].phut} phut")
