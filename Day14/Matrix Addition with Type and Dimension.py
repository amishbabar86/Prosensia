class MatrixDimensionError(Exception):
    pass

def add_matrices(matrix1, matrix2):
    if not all(isinstance(row, list) for row in [matrix1, matrix2]) or not all(isinstance(elem, (int, float)) for row in matrix1 + matrix2 for elem in row):
        raise TypeError("Matrices must be lists of lists containing only numbers.")

    if len(matrix1) != len(matrix2) or any(len(row1) != len(row2) for row1, row2 in zip(matrix1, matrix2)):
        raise MatrixDimensionError("Matrices must have the same dimensions.")

    return [[elem1 + elem2 for elem1, elem2 in zip(row1, row2)] for row1, row2 in zip(matrix1, matrix2)]


matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]
result = add_matrices(matrix1, matrix2)
print(result)  
