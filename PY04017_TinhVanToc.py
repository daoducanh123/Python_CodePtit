
from datetime import datetime

class Person:
    def __init__(self, name, place, endTime, speed):
        self.ma = ""
        self.name = name
        self.place = place
        self.endTime = endTime
        self.speed = speed

    def Ma(self):
        arrPlace = self.place.strip().upper().split()
        arrName = self.name.strip().upper().split()

        for i in range(len(arrPlace)):
            self.ma += arrPlace[i][0]

        for i in range(len(arrName)):
            self.ma += arrName[i][0]


n = int(input())
listPerson = []

for _ in range(n):
    name = input().strip()
    place = input().strip()
    endTimeStr = input().strip()

    endTime = datetime.strptime(endTimeStr, "%H:%M")
    startTime = datetime.strptime("06:00", "%H:%M")

    minutes = (endTime - startTime).total_seconds() / 60
    speed = round(120 * 60 / minutes)

    person = Person(name, place, endTime, speed)
    person.Ma()
    listPerson.append(person)

listPerson.sort(key=lambda x: x.endTime)

for p in listPerson:
    print(f"{p.ma} {p.name} {p.place} {p.speed} Km/h")
