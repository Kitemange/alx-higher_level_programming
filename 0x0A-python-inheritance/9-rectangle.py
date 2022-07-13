#!/usr/bin/python3
""" importing class BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class Rectangle that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Instantiate of width and height.

        Args:
            width (int): Rectangle width
            height (int): Rectangle height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__height = height
        self.__width = width

    def area(self):
        """Area of the Rectangle"""
        return self.__width * self.__height
    
    def __str__(self) -> str:
        """ Special method that returns the printable string """
        return super().__str__()
