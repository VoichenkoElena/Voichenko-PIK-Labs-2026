import math
from .figure import Figure

class Tetrahedron(Figure):
    def __init__(self, edge):
        super().__init__("Тетраэдр")
        self.edge = edge

    @property
    def edge(self):
        return self.__edge

    @edge.setter
    def edge(self, value):
        if value <= 0:
            raise ValueError("Ребро должно быть > 0")
        self.__edge = value

    def volume(self):
        return (self.edge ** 3) / (6 * math.sqrt(2))

    def area(self):
        return math.sqrt(3) * (self.edge ** 2)