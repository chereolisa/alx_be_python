import math


class Shape:
    """
    Base class for all geometric shapes.
    The area() method is deliberately not implemented
    so that concrete subclasses must override it.
    """
    def area(self):
        raise NotImplementedError("Subclasses must implement area() method")


class Rectangle(Shape):
    """
    Rectangle shape - inherits from Shape.
    """
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self) -> float:
        """Return the area of the rectangle: length × width"""
        return self.length * self.width


class Circle(Shape):
    """
    Circle shape - inherits from Shape.
    """
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        """Return the area of the circle: π × radius²"""
        return math.pi * self.radius ** 2


# Optional: small demonstration when the file is run directly
if __name__ == "__main__":
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")