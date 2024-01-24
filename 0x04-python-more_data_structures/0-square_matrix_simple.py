#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return None
    res = [[matrix[i][j] ** 2 for j in range(len(matrix[i]))]
           for i in range(len(matrix))]
    return res
