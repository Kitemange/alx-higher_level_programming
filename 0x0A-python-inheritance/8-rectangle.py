#!/usr/bin/python3
"""Geometry module.

Author: Bryan Mutheke
"""


class BaseGeometry:
    """An empty class."""

    def area(self):
        """Raise an exception.

        Raises:
            Exception: uni,plemented area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the inputs.

        Args:
            name(str) : arg 1
            value (int): arg 2

        Raises:
            TypeError: Not an integer
            ValueError: Less than 0

        Returns:
            _type_: Value
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} name must be greater than 0".format(name))


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
