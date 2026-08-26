'''Write a program to create an abstract class Shape with abstract methods
calculateArea() and calculatePerimeter(). Create subclasses Circle and Triangle
that extend the Shape class and implement the respective methods to calculate
the area and perimeter of each shape.'''
from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def calculateArea(self):
        pass
    @abstractmethod
    def calculatePerimeter(self):
        pass
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def calculateArea(self):
        return 22/7*self.radius**2
    def calculatePerimeter(self):
        return 2*22/7*self.radius
class triangle(shape):
    def __init__(self,a,b,c,height):
        self.a=a
        self.b=b
        self.c=c
        self.height=height
    def calculateArea(self):
        return 1/2*self.b*self.height
    def calculatePerimeter(self):
        return self.a+self.b+self.c
obj1=circle(6)
obj2=triangle(6,8,6,15)
print("Area of the circle:",obj1.calculateArea())
print("perimeter of the circle:",obj1.calculatePerimeter())
print("Area of the triangle:",obj2.calculateArea())
print("perimeter of the triangle:",obj2.calculatePerimeter())
    
