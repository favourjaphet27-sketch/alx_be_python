import math


class Shape:
    # Base class representing a generic shape
    def area(self):
        # method to calculate the area of the shape. Must be overriden by derived classes.
        raise NotImplementedError("area() must be implemented in the subclass")


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        # Calculate and return the area of the rectangle
        return self.length * self.width


class Circle(Shape):
    # Represents a circle
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle"""
        return math.pi * self.radius ** 2
