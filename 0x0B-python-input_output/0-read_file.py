#!/usr/bin/python3
"""
File: 0-read_file.py
Desc: This module contains one function; read_file(filename="")
Author: Florence Muthoka
"""


def read_file(filename=""):
    """
    reads a text file (UTF8) and print it
    """
    with open(filename, "r", encoding="UTF-8") as f:
        for line in f:
            print(line, end='')
