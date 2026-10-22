
import math
from decimal import Decimal

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, point):
        dx = float(self.x - point.x)
        dy = float(self.y - point.y)
        return math.sqrt(dx * dx + dy * dy)


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def dienTich(self):
        a = self.b.distance(self.c)
        b = self.a.distance(self.c)
        c = self.a.distance(self.b)

        if a + b <= c or a + c <= b or b + c <= a:
            return -1

        res = (a + b + c) * (-a + b + c) * \
              (a - b + c) * (a + b - c)

        return math.sqrt(max(0, res)) / 4


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        arr = input().split()

        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        p3 = Point(Decimal(arr[4]), Decimal(arr[5]))

        tg = Triangle(p1, p2, p3)
        s = tg.dienTich()

        if s < 0:
            print("INVALID")
        else:
            print(f"{s:.2f}")
