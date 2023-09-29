import numbers
from abc import ABC, abstractmethod
from math import pi

"""
abc : module name (built-in module)
ABC : Abstract class in abc module
abstractmethod : annotations that can be given to abstract methods
"""


class Volume(ABC):

    @abstractmethod
    def volume(self):
        pass


class Shape(ABC):

    def __init__(self):
        self.name = type(self).__name__

    @abstractmethod
    def area(self) -> numbers:
        pass

    def __str__(self):
        return f"{type(self).__name__}{self.__dict__}"


class Square(Shape):

    def __init__(self, side: numbers):
        super().__init__()
        self.side = side

    def area(self) -> numbers:
        return self.side * self.side


class Circle(Shape):

    def __init__(self, radius: numbers):
        super().__init__()
        self.radius = radius

    def area(self) -> numbers:
        return pi * self.radius * self.radius


class Rectangle(Shape):

    def __init__(self, length: numbers, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self) -> numbers:
        return self.length * self.width


class Cube(Shape, Volume):

    def __init__(self, side: numbers):
        super().__init__()
        self.side = side

    def area(self) -> numbers:
        return 6 * self.side * self.side

    def volume(self):
        return self.side * self.side * self.side


class Cylinder(Shape, Volume):

    def __init__(self, radius: numbers, height: numbers):
        super().__init__()
        self.radius = radius
        self.height = height

    def area(self) -> numbers:
        return 2 * pi * self.radius * (self.height + self.radius)

    def volume(self):
        return pi * self.radius * self.radius * self.height


square1 = Square(5)
rectangle1 = Rectangle(14.6, 8.99)
circle1 = Circle(4.56)
cube1 = Cube(5)
cylinder1 = Cylinder(3.35, 12.46)

print(square1)
print(rectangle1)
print(circle1)
print(cube1)
print(cylinder1)

print(square1.area())
print(rectangle1.area())
print(round(circle1.area(), 2))
print(cube1.area())
print(cube1.volume())
print(round(cylinder1.area(), 2))
print(round(cylinder1.volume(), 2))
