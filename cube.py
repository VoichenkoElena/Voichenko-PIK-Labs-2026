from .figure import Figure

class Cube(Figure):
    def __init__(self, side):
        super().__init__("Куб")
        self.side = side

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Сторона должна быть числом")
        if value <= 0:
            raise ValueError("Сторона должна быть > 0")
        self.__side = value
    
    def volume(self):
        return self.side ** 3

    def area(self):
        return 6 * (self.side ** 2)

    def get_type(self):
        return "Это куб (переопределенный метод)"