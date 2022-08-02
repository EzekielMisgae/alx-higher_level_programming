#!/usr/bin/python3
"""
This module contains a class Student that defines a student
"""


class Student():
    """
    Student class
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__  # or return vars(obj)
