import math
from .figure import Figure

class Cone(Figure):
    def __init__(self, radius, height):
        super().__init__("Конус")
        self.radius = radius
        self.height = height

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Радиус должен быть > 0")
        self.__radius = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Высота должна быть > 0")
        self.__height = value

    def volume(self):
        return (1/3) * math.pi * (self.radius ** 2) * self.height

    def area(self):
        l = math.sqrt(self.radius ** 2 + self.height ** 2)
        return math.pi * self.radius * (self.radius + l)