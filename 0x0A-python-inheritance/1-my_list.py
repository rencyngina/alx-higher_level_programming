#!/usr/bin/python3
"""
This is a class that inherits from the class list
"""


class MyList(list):
    """derived class"""

    def print_sorted(self):
        """Prints sorted list in ascending order"""
        print(sorted(self))
