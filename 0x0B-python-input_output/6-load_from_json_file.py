#!/usr/bin/python3
"""
This module contains a function that creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """Create an Object from a JSON file"""
    with open(filename, 'r') as f:
        # load: lee un archivo y convierte los datos en JSON(objeto)
        return json.load(f)
