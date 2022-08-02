#!/usr/bin/python3
"""This module contains the function pascal_triangle"""


def pascal_triangle(n):
    """The Pascal Triangle function"""
    mtx = []
    aux = 0
    for i in range(n):
        mtx.append([])
    for i in range(n):
        for x in range(i + 1):
            if x == 0 or x == i:
                mtx[i].append(1)
            else:
                aux = mtx[i - 1][x] + mtx[i - 1][x - 1]
                mtx[i].append(aux)
        """ print(mtx[i]) """
    return mtx
