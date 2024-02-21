#!/usr/bin/python3

""" Technical interview preparation """


def pascal_triangle(n):
    """ implementation of pascal triangle """
    if n <= 0:
        return []
    pas = [[1]]
    if n == 1:
        return pas
    for i in range(n - 1):
        if len(pas) == 1:
            pas.append([1, 1])
        else:
            temp = [pas[i][j] + pas[i][j + 1] for j in range(len(pas[i]) - 1)]
            temp.insert(0, 1)
            temp.append(1)
            pas.append(temp)
    return pas
