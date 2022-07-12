#!/usr/bin/python3
"""Author: Bryan."""


def inherits_from(obj, a_class):
    """A function that returns True if the object is
    an instance of a class that inherited (directly or indirectly)
    from the specified class;
    otherwise False.

    Args:
        obj(any): object of the class
        a_class(type): describes the class

    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
