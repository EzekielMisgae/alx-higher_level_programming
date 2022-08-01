#!/usr/bin/python3
"""This module contains the add_attribute method"""


def add_attribute(obj, key, value):
    """Adds a new attribute to an object if it’s possible"""
    if not hasattr(obj, '__dic__'):
        raise TypeError("can't add new attribute")

    setattr(obj, key, value)
