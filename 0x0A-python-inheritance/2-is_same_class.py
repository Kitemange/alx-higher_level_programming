#!/usr/bin/python3
"""Author : Bryan."""


def is_same_class(obj, a_class):
    """
    Return True/False if obj is a type of a_class.

    Args:
        obj (_type_): Object.
        a_class : Class Type.

    Returns:
        True if Obj is a_class
        else
            FALSE
    """
    return type(obj) is a_class
