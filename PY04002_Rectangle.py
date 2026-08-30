import math
from typing import override
from abc import ABC, abstractmethod

import sys

class Rectangle:
    def __init__(self, length, width,color):
        self.__length = length
        self.__width = width
        self.__color = color[0:1].upper() + color[1:].lower() # color.capitalize()

    def perimeter(self):
        return (self.__length + self.__width) * 2
    def area(self):
        return self.__length * self.__width
    def color(self):
        return self.__color

arr = input().split()
if int(arr[0]) > 0 and int(arr[1]) > 0:
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
    print("{} {} {}".format(r.perimeter(), r.area(), r.color()))
else:
    print("INVALID")
sys.exit()


if __name__ == '__main__':
    arr = input().split()
    r = Rectangle(int(arr[0]), int(arr[1]), int(arr[2]))

    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
    t = int(input())
    string = string(t)