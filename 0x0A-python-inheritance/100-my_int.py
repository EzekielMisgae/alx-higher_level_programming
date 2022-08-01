#!/usr/bin/python3
"""This module contains the MyInt class"""


class MyInt(int):
    """
    MyInt class
    """

    def __eq__(self, value):
        """If are equals, inverting it"""
        return int(self) != int(value)

    def __ne__(self, value):
        """If are not equals, inverting it"""
        return int(self) == int(value)
