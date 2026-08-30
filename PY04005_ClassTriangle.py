import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Triangle:
    def __init__(self, c1, c2, c3):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3

    def ChuVi(self):
        res = self.c1 + self.c2 + self.c3
        print(f"{res:.3f}")

    def Check(self):
        if self.c1 + self.c2 <= self.c3 or self.c1 + self.c3 <= self.c2 or self.c2 + self.c3 <= self.c1:
            return False
        else:
            return True


test = int(input())
while test > 0:
    x1, y1, x2, y2, x3, y3 = map(float, input().split())
    p1 = Point(x1,y1)
    p2 = Point(x2,y2)
    p3 = Point(x3,y3)

    dx1 = p3.x-p2.x
    dy1 = p3.y-p2.y
    c1 = math.sqrt(dx1 * dx1 + dy1 * dy1)

    dx2 = p3.x-p1.x
    dy2 = p3.y-p1.y
    c2 = math.sqrt(dx2 * dx2 + dy2 * dy2)

    dx3 = p1.x-p2.x
    dy3 = p1.y-p2.y
    c3 = math.sqrt(dx3 * dx3 + dy3 * dy3)


    triangle = Triangle(c1,c2,c3)
    
    if triangle.Check():
        triangle.ChuVi()
    else:
        print("INVALID")

    test -= 1