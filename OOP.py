from typing import override
from abc import ABC, abstractmethod


class Animal(ABC):
    #Field
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def Sound(self):
        pass

class Dog(Animal):
    @override
    def Sound(self):
        print(f"{self.name} {self.age} years old goes Woof!")



if __name__ == '__main__':
    dog = Dog("Hello",19)
    dog.Sound()