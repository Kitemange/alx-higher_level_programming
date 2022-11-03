#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    A function that replaces an element in a list at
    a specific position without modifying the original list

    Args:
        my_list ():contains a list of numbers
        idx (): POsition to alter in the list
        element (): Value to be placed in the idx

    Returns:
        copy: copy of my_list containing elelmt in the idx position
        my_list: original list
    """
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        copy = my_list.copy()
        copy[idx] = element
        return copy
