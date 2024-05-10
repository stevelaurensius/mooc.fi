# Please write a function named block_correct(sudoku: list, row_no: int,
# column_no: int), which takes a two-dimensional array representing a sudoku grid, and
# two integers referring to the row and column indexes of a single square,
# as its arguments. Rows and columns are indexed from 0.

# The function should return True or False depending on whether the 3 by 3 block to the
# right and down from the given indexes is filled in correctly. That is, whether the block
# contains each of the numbers 1 to 9 at most once.

# Notice that this function does not strictly follow the rules of sudoku. In a real game of
# sudoku there are only 9 blocks to check, and these are located at indexes (0, 0), (0, 3), (0,
# 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3) and (6, 6). Such restrictions on indexes should not be
# implemented here.


def block_correct(sudoku: list, row_no: int, column_no: int):
    block_list = sudoku[row_no][column_no:column_no + 3] + sudoku[row_no + 1][column_no:column_no + 3] + sudoku[row_no + 2][column_no:column_no + 3]
    without_zero = [x for x in block_list if x != 0]
    checker = set(without_zero)
    if len(checker) == len(without_zero):
        return True
    else:
        return False
