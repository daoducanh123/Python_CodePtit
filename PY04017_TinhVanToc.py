from datetime import datetime

class Person:
    def __init__(self, name, place, speed):
        self.ma = ""
        self.name = name
        self.place = place
        self.speed = speed
        
    def Ma(self):
        arrPlace = self.place.strip().upper().split()
        arrName = self.name.strip().upper().split()
        for i in range (len(arrPlace)):
            self.ma += arrPlace[i][0]
        for i in range (len(arrName)):
            self.ma += arrName[i][0]     
n = int(input())
listPerson = list()
for _ in range(n):
    name = input()
    place= input()
    
    # thoi gian
    endTimeStr = input()
    endTime = datetime.strptime(endTimeStr, "%H:%M")
    startTime = datetime.strptime("06:00", "%H:%M")
    hours = (endTime-startTime).total_seconds()/3600
    speed = round(120 / hours,0)
    
    person = Person(name , place , speed )
    person.Ma()    
    listPerson.append(person)
listPerson = sorted(listPerson, key = lambda x: -x.speed)
for p in listPerson:
    print (f"{p.ma} {p.name} {p.place} {p.speed:.0f} Km/h")