from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Abstract base class for shapes"""
    
    @abstractmethod
    def area(self) -> float:
        """Calculate the area of the shape"""
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        """Calculate the perimeter of the shape"""
        pass
    
    @abstractmethod
    def describe(self) -> str:
        """Return a description of the shape"""
        pass

class Circle(Shape):
    """Concrete implementation of a circle"""
    
    def __init__(self, radius: float):
        self.radius = radius
    
    def area(self) -> float:
        return math.pi * self.radius ** 2
    
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius
    
    def describe(self) -> str:
        return f"Circle with radius {self.radius}"

class Rectangle(Shape):
    """Concrete implementation of a rectangle"""
    
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    
    def area(self) -> float:
        return self.width * self.height
    
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)
    
    def describe(self) -> str:
        return f"Rectangle with width {self.width} and height {self.height}"

def main():
    # This would raise TypeError because Shape is abstract
    #shape = Shape()
    
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    
    shapes = [circle, rectangle]
    
    for shape in shapes:
        print(f"\n{shape.describe()}")
        print(f"Area: {shape.area():.2f}")
        print(f"Perimeter: {shape.perimeter():.2f}")

if __name__ == "__main__":
    main()