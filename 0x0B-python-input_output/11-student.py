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

    def to_json(self, attrs=None):
        """JSON representation"""
        if attrs is None:
            return self.__dict__  # or return vars(obj)
        else:
            attrs_dic = {}
            for i in self.__dict__:
                if i in attrs:
                    attrs_dic[i] = self.__dict__[i]
            return attrs_dic

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        json_dict = vars(self)
        for key, value in json.items():
            json_dict[key] = value
