#!/usr/bin/python3
"""This module contains the Rectangle Class."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """The Rectangle subclass inherits from BaseGeometry class."""

    def __init__(self, width, height):
        """Instantiation with width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Return Rectangle's area
        """
        return self.__width * self.__height

    def __str__(self):
        """str() should return, the following rectangle description

        Returns:
            str: [Rectangle] <width>/<height>
        """
        return '[Rectangle] ' + str(self.__width) + '/' + str(self.__height)
