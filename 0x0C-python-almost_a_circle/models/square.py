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
        return str_res

    
    @property
    def size(self):
        """Size getter"""
        return self.width
    
    @size.setter
    def size(self, value):
        """Set the size of the square"""
        self.width = value
        self.height = value
    
    def update(self, *args, **kwargs):
        """
        Updates square class and assigns an 
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

    def to_dictionary(self):
        """ Returns the dictionary representation of a Square """
        list = ['x', 'y', 'id', 'size']
        Dict = {}

        for k in list:
            Dict[k] = getattr(self, k)

        return Dict
