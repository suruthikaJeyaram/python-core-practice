'''Write a program to create an abstract class Animal with an abstract method
called sound(). Create subclasses Lion and Tiger that extend the Animal class
and implement the sound() method to make a specific sound for each animal.'''
from abc import ABC,abstractmethod
class animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Lion(animal):
    def sound(self):
        print("roar")
class Tiger(animal):
    def sound(self):
        print("grrrr")
   
obj1=Lion()
obj2=Tiger()

obj1.sound()
obj2.sound()
