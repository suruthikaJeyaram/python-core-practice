'''Write the abstract class Shape , the concrete classes Circle and Rectangle , and
the code to display the areas.'''
from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def calculateArea(self):
        pass
class circle(shape):
    def __init__(self,radius):
        self.radius=radius

    def calculateArea(self):
          return 22/7*self.radius**2
    
class rectangle(shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def calculateArea(self):
        return self.length*self.width
    
obj1=circle(6)
obj2=rectangle(4,5)
print(obj1.calculateArea())
print(obj2.calculateArea())