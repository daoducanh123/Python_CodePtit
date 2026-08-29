
import math
from decimal import Decimal
# 2
# 0 0 0 5
# 0 199 5 6

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, Point):
        dx = self.x - Point.x
        dy = self.y - Point.y
 
        res = math.sqrt (dx *dx + dy*dy)
        string = f"{res:.4f}" #giong string format trong java
        return string


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split() # arr = ["0", "0", "0", "5"]
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1