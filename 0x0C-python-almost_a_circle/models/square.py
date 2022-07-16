#!/usr/bin/python3
""" This module contains the class Square,
inherited from class Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square Class """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes instances """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        str_name = ("[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x,self.y,self.__width,self.__height))
        return str_name

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter size """
        self.width = value
        self.height = value

    def __str__(self):
        """String method for rectangle class"""
        str_res = ("[Square] ({}) {}/{} - {}"
                   .format(self.id, self.x, self.y, self.width))
        return str_res
    
    def update(self, *args, **kwargs):
        """Updates the public class
        Args:
            *args(any): the list of arguments - no-keyworded arguments
            **kwargs(any):
        """
        if args:
            attributes = ["id", "size", "x", "y"]
            for i, j in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], j)
        else:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    setattr(self, k, v)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Square """
        list_atr = ['id', 'x', 'size', 'y']
        dict_res = {}

        for key in list_atr:
            if key == 'size':
                dict_res[key] = getattr(self, 'width')
            else:
                dict_res[key] = getattr(self, key)

        return dict_res
