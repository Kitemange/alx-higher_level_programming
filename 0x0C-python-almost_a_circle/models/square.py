#!/usr/bin/python3
"""Square."""
from models.rectangle import Rectangle
from models.base import Base

class Square(Rectangle):
    """A square class inheriting from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructs the square's attributes"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String method for rectangle class"""
        str_res = ("[Square] ({}) {}/{} - {}/{}"
                   .format(self.id, self.x, self.y, self.width,self.height))

    
    @property
    def size(self):
        """"""
        return self.width
    
    @size.setter
    def size(self, value):
        """Set the size of the square"""
        self.width = value
        self.height = value