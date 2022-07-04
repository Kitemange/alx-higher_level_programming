#!/usr/bin/python3
"""Integers addition"""

def add_integer(a, b=98):
    """Function to add two numbers

    args:
        a = first input
        b = second input
    
    Returns:
        The addition of the valuea a and b
    
    Raises:
        TypeError: If a or b aren't integer and/or float numbers
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    
    a = int(a)
    b = int(b)
    return a + b
