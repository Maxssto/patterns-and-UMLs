from abc import ABC, abstractmethod


class Shape(ABC):
    """"Shape выполняет функцию абстракции"""
    def __init__(self, implementation):
        self.implementation = implementation

    def show_colour(self):
        return self.implementation.paint()


class Circle(Shape):
    """Конкретная абстракция круг"""
    def name(self):
        print("This is circle")


class Square(Shape):
    """Конкретная абстракция квадрат"""
    def name(self):
        print("This is square")


class Colour(ABC):
    """Интерйес реализации"""
    @abstractmethod
    def paint(self):
        pass


class Red(Colour):
    """Интерйес конкретной реализации (красный)"""
    def paint(self):
        print("painted in red")


class Blue(Colour):
    """Интерйес конкретной реализации (синий)"""
    def paint(self):
        print("painted in blue")


if __name__ == "__main__":
    red = Red()
    red_circle = Circle(red)
    red_circle.name()
    red_circle.show_colour()
    print("----------------")
    blue = Blue()
    blue_square = Square(blue)
    blue_square.name()
    blue_square.show_colour()
