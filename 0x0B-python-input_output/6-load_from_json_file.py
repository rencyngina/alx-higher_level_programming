#!/usr/bin/python3
"""
File name: 6-load_from_json_file.py
Author: Florence Muthoka
"""

import json


def load_from_json_file(filename):
    """
    Creates an Object from a “JSON file”
    """
    with open(filename, "r") as f:
        return json.load(f)
