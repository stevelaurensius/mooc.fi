# Please write a function named column_correct(sudoku: list, column_no: int),
# which takes a two-dimensional array representing a sudoku grid, and an integer referring
# to a single column, as its arguments. Columns are indexed from 0.

# The function should return True or False, depending on whether the column is filled in
# correctly, that is, whether it contains each of the numbers 1 to 9 at most once.

def column_correct(sudoku: list, column_no: int):
    transpose_list = [row[column_no] for row in sudoku]
    without_zero = [x for x in transpose_list if x != 0]
    checker = set(without_zero)
    if len(checker) == len(without_zero):
        return True
    else:
        return False
