#!/usr/bin/python3
"""
File name: 11-student.py
Author: Florence muthoka
"""


class Student:
    """
    Reoresentation of the class Student
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialization of the class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance
        """
        if type(attrs) == list and all(type(i) == str for i in attrs):
            return ({key: getattr(self, key)
                    for key in attrs if hasattr(self, key)})
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        """
        for key, value in json.items():
            setattr(self, key, value)
