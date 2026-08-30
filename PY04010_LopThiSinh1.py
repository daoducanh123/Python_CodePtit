class ThiSinh:
    def __init__(self, name, dob, d1,d2,d3):
        self.name = name
        self.dob = dob
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        self.sum = self.d1+self.d2+self.d3


    
    
#input mỗi dòng
name = input()
dob = input()
d1 =  float(input())
d2 = float(input())
d3 = float(input())

thiSinh = ThiSinh(name, dob, d1,d2,d3)
resSum = f"{thiSinh.sum:.1f}"
print(f"{thiSinh.name} {thiSinh.dob} {resSum}")
