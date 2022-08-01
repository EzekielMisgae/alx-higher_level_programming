#!/usr/bin/python3
"""This module contains the BaseGeometry Class."""


class BaseGeometry:
    """
    BaseGeometry Class.
    """

    def area(self):
        """
        Public instance method that raises an Exception with the message.
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Public instance method that validates value."""
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
