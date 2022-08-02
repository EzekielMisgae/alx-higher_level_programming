#!/usr/bin/python3
"""This module contains a function to add text on text file"""


def append_write(filename="", text=""):
    """Write at the end a text file"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
