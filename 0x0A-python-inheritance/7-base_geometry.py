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
        return value
