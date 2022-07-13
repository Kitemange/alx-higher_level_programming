#!/usr/bin/python3
"""My integer"""


class MyInt(int):
    """A class that inherits from int"""
    
    def __eq__(self, __x: object):
        """Not equating the operator"""
        return super().__eq__(__x)
    
    def __ne__(self, __x: object):
        """Equating the operator"""
        return super().__ne__(__x)
