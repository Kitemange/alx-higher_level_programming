#!/usr/bin/python3
"""Author : Bryan."""


class MyList (list):
    """

    Class inherits from List.

    Args:
        list: inherited into this class
    """

    def print_sorted(self):
        """Print out a sorted list."""
        print(sorted(self))
