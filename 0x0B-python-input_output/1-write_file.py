#!/usr/bin/python3
"""
file function is writen
"""


def write_file(filename="", text=""):
    """
    Writes into file , create it and don't exit
    """
    with open(filename, mode="w", encoding="UTF-8") as f:
        return(f.write(text))
