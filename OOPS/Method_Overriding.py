# Run-time Polymorphism :

class Shape:
    def calcArea(self):
        raise NotImplementedError("The class is not implemented !!")

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def calcArea(self):
        area = self.width*self.height
        print("Area of the Rectangle is : "+str(area))
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def calcArea(self):
        area = 3.14*self.radius*self.radius
        print("Area of the square is : "+str(area))

class Square(Shape):
    def __init__(self,side):
        self.side = side
    def calcArea(self):
        area = self.side*self.side
        print("Area of the square is : "+str(area))
rectangle = Rectangle(10,20)
circle = Circle(10)
square = Square(20)
rectangle.calcArea()
circle.calcArea()
square.calcArea()