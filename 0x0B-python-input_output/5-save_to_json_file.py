#!/usr/bin/python3
"""
This module contains a function that writes an Object to a
text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """Write an Objet to a text file (.json)"""
    with open(filename, 'w') as f:
        # dump: a partir de un objeto, crea un JSON y lo guarda en un archivo
        json.dump(my_obj, f)
        """ json_data = json.dumps(my_obj)
        f.write(json_data) """
