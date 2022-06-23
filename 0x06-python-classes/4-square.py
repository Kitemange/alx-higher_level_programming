#!/usr/bin/python3

class Square:
    """Square class with a private attribute -
    size.
    """
    def __init__(self, size = 0):
        """Initializes the size variable as a private
        instance artribute
        """
        self.__size = size

    @property
    def size(self):
        """Retrive Size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter to set it (value)"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns the current square area"""
        return(self.__size ** 2)
