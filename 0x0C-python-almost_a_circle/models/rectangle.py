#!/usr/bin/python3
"""First Rectangle"""

from models.base import Base


class Rectangle(Base):
    """A rectangle class that inherits from
    the base class

    Args:
        Base(model): the inherited model
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("width must be > 0")
        if type(value) is not int:
            raise TypeError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("height must be > 0")
        if type(value) is not int:
            raise TypeError("height must be an integer")
        self.__height = value

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, value):
        if value < 0:
            raise ValueError("x must be >= 0")
        if type(value) is not int:
            raise TypeError("x must be an integer")
        self.__x = value

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, value):
        if value < 0:
            raise ValueError("y must be >= 0")
        if type(value) is not int:
            raise TypeError("y must be an integer")
        self.__y = value
    
    def area(self):
        return self.__height * self.__width
    
    def display(self):
        print("\n" * self.y,  end="")
        print((" " * self.x + "#" * self.__width + '\n') * self.__height, end="")
    
    def __str__(self):
        """String representation of the rectangle class"""
        str_res = "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self.y, self.__width, self.__height)
        return str_res
    
    def update(self, *args, **kwargs):
        """
        Updates rectangle class and assigns an 
        argument to each attribute

        Args:
            *args(args):
            *kwargs(kwargs):
        """
        if args != None and len(args) != 0:
            attributes= ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

        
