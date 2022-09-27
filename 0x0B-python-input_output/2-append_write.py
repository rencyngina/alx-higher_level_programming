#!/usr/bin/python3
"""
The file name is 2-append_write.py
Author: Florence Muthoka
"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    """
    with open(filename, mode="a", encoding="UTF-8") as f:
        return f.write(text)
