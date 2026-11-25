from abc import ABC, abstractmethod

class Figure(ABC):
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @abstractmethod
    def volume(self):
        pass

    @abstractmethod
    def area(self):
        pass

    def get_type(self):
        return self.name

    def __str__(self):
        return f"{self.name}: Объем = {self.volume():.2f}, Площадь = {self.area():.2f}"