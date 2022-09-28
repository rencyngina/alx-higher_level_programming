#!/usr/bin/python3
"""
contains the class BaseGeometry
"""


class BaseGeometry:
    """a class with a function that raises exception"""
    def area(self):
        """A public instance method that raises an exception"""
        raise Exception("area() is not implemented")
