#!/usr/bin/python3
"""This module contains the inherits_from function"""


def inherits_from(obj, a_class):
    """Returns True if obj inherits from a_class, False"""
    return isinstance(obj, a_class) and type(obj) != a_class
