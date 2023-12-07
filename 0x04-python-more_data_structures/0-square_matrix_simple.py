#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for i in matrix:
        row = []
        for j in i:
            row.append(j ** 2)
        new.append(row)
    return(new)
