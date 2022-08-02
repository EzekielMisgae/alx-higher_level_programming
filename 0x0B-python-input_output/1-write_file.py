#!/usr/bin/python3
"""This module contains a function to write on text file"""


def write_file(filename="", text=""):
    """Write on a text file"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
