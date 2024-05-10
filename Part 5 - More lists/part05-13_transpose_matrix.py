# Please write a function named transpose(matrix: list), which takes a
# two-dimensional integer array, i.e., a matrix, as its argument. The function
# should transpose the matrix. Transposing means essentially flipping the matrix
# over its diagonal: columns become rows, and rows become columns.

# You may assume the matrix is a square matrix, so it will have an equal number
# of rows and columns.

def transpose(matrix):
    size = len(matrix)
    for i in range(size):
        for j in range(i + 1, size):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
