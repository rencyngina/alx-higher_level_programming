#!/usr/bin/python3
"""
You need to returns the list of available attributes
and methods of an object
"""


def lookup(obj):
    """returns all attributes and methods of an object"""
    fun = dir(obj)
    return fun
