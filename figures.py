#
#
# Создайте класс любых геометрических фигур, где на выход мы получаем характеристики фигуры. Каждый
# экземпляр должен иметь атрибуты, которые зависят от выбранной фигуры. Например, для прямоугольника
# это будут аргументы x, y, width и height.
#
# Кроме того вы должны иметь возможность передавать эти атрибуты при создании объекта класса.
#
# Создайте метод, который возвращает атрибуты вашей фигуры в виде строки.

class Geometric_shapes:
    pass

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def get_parametrs_Rectangle(self):
        return "Rectangle(" + str(self.width) + ',' + str(self.height) + ')'

class Square:
    def __init__(self, width):
        self.width = width
    def get_parametr_Square(self):
        return "Square(" + str(self.width) + ')'

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_parametr_Circle(self):
        return "Circle(" + str(self.radius) + ')'

rect_1 = Rectangle(3, 4)

square_1 = Square(5)

circle = Circle(6)

figures = [rect_1, square_1, circle]

for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_parametr_Square())
    elif isinstance(figure, Circle):
        print(figure.get_parametr_Circle())
    else:
        print(figure.get_parametrs_Rectangle())