#!/usr/bin/python3
"""This module contains a function that reads from a file."""


def read_file(filename=""):
    """Read from a file.

    Args:
        filename (str): Filename "".
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        print(f.read(), end="")
