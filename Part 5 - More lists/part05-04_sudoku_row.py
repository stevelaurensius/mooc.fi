# Please write a function named row_correct(sudoku: list, row_no: int), which
# takes a two-dimensional array representing a sudoku grid, and an integer referring to a
# single row, as its arguments. Rows are indexed from 0.

# The function should return True or False, depending on whether the row is filled in
# correctly, that is, whether it contains each of the numbers 1 to 9 at most once.

def row_correct(sudoku: list, row_no: int):
    without_zero = [x for x in sudoku[row_no] if x != 0]
    checker = set(without_zero)
    if len(checker) == len(without_zero):
        return True
    else:
        return False
