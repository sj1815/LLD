from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __init__(self, name: str):
        self._name = name

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass  

    def describe(self) -> None:
        print(f"Shape: {self._name}, Area: {self.area():.2f}, Perimeter: {self.perimeter():.2f}")

class Circle(Shape):
    def __init__(self, radius: float):
        super().__init__("Circle")
        self._radius = radius

    def area(self) -> float:
        return math.pi * self._radius * self._radius\
        
    def perimeter(self) -> float:
        return 2 * math.pi * self._radius        
        
class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        super().__init__("Rectangle")
        self._width = width
        self._height = height

    def area(self) -> float:
        return self._height * self._width
    
    def perimeter(self) -> float:
        return 2 * (self._height + self._width)

if __name__ == "__main__":
    circle = Circle(5.0)
    circle.describe()

    rectangle = Rectangle(4.0, 6.0)
    rectangle.describe()  