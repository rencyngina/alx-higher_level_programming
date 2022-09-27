#!/usr/bin/python3
"""
File name: 4-from_json_string.py
Author:Florence Muthoka
"""

import json


def from_json_string(my_str):
    """
    eturns an object (Python data structure) represented by a
    JSON string
    """
    return json.loads(my_str)
