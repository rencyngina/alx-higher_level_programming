#!/usr/bin/python3
"""
This file contains a derived class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a derived class"""
    def __init__(self, width, height):
        """instantiates derived class attributes"""
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of the class Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns description of the class Rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
