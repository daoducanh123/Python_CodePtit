class CaThi:
    def __init__ (self,id,date,time,phong):
        self.id = id 
        self.date = date
        self.time= time
        self.phong=phong
        
        
    # tostring cua java
    def __str__ (self):
        return f"{self.id} {self.date} {self.time} {self.phong}"
     
f = open("CATHI.in", "r")
t= int(f.readline())

a = []
for i in range(t):
    id = f"C{i+1:03d}"
    date = f.readline().strip()
    time = f.readline().strip()
    phong = f.readline().strip()
    
    a.append(CaThi(id,date,time,phong))
    
a= sorted(a,key = lambda x: (x.date[6:], x.date[3:5], x.date[:2], x.time[:2],x.time[3:], x.id))

for i in a:
    print(i)