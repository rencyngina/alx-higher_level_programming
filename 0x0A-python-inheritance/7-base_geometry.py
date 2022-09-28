#!/usr/bin/python3
"""
BaseGeometry class
"""


class BaseGeometry:
    """A class with public method that raises exception"""
    def area(self):
        """A public instance method that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A public instance method that validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
