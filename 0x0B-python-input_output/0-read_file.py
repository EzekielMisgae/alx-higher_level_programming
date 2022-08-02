#!/usr/bin/python3
"""This module contains a function to read a text file"""


def read_file(filename=""):
    """Read a text file"""
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
