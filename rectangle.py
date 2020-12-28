#
#
# Напишите код для описания геометрической фигуры.
# Создайте класс «прямоугольник» с помощью метода  __init__(). На выходе в консоли вам необходимо получить
# длину и ширину с итоговыми значениями.



class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def get_parametrs_Rectangle(self):
        return "Rectangle: " + "width = " + str(self.width) + ',' + " height = " + str(self.height)

rect_1 = Rectangle(3, 4)

print(rect_1.get_parametrs_Rectangle())