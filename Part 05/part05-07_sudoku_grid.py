# Please write a function named sudoku_grid_correct(sudoku: list), which takes a
# two-dimensional array representing a sudoku grid as its argument. The function should
# use the functions from the three previous exercises to determine whether the complete
# sudoku grid is filled in correctly. Copy the functions from the exercises above into your
# Python code file for this exercise.

# The function should check each of the nine rows, columns and 3 by 3 blocks in the grid. If
# all contain each of the numbers 1 to 9 at most once, the function returns True. If a single
# one is filled in incorrectly, the function returns False.

# The image of a sudoku grid above these exercises has the nine blocks within the grid
# indicated with thicker borders. These are the blocks the function should check, and they
# begin at the indexes (0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3) and (6, 6).

def row_correct(sudoku: list, row_no: int):
    without_zero = [x for x in sudoku[row_no] if x != 0]
    checker = set(without_zero)
    if len(checker) == len(without_zero):
        return True
    else:
        return False


def column_correct(sudoku: list, column_no: int):
    transpose_list = [row[column_no] for row in sudoku]
    without_zero = [x for x in transpose_list if x != 0]
    checker = set(without_zero)
    if len(checker) == len(without_zero):
        return True
    else:
        return False


def block_correct(sudoku: list, row_no: int, column_no: int):
    block_list = (sudoku[row_no][column_no:column_no + 3] + sudoku[row_no + 1][column_no:column_no + 3] +
                  sudoku[row_no + 2][column_no:column_no + 3])
    without_zero = [x for x in block_list if x != 0]
    checker = set(without_zero)
    if len(checker) == len(without_zero):
        return True
    else:
        return False


def sudoku_grid_correct(sudoku: list):
    counter = 0
    row_check = []
    column_check = []
    block_check = []
    while counter < 9:
        row_check.append(row_correct(sudoku, counter))
        column_check.append(column_correct(sudoku, counter))
        counter += 1
    block_check.append(block_correct(sudoku, 0, 0))
    block_check.append(block_correct(sudoku, 0, 3))
    block_check.append(block_correct(sudoku, 0, 6))
    block_check.append(block_correct(sudoku, 3, 0))
    block_check.append(block_correct(sudoku, 3, 3))
    block_check.append(block_correct(sudoku, 3, 6))
    block_check.append(block_correct(sudoku, 6, 0))
    block_check.append(block_correct(sudoku, 6, 3))
    block_check.append(block_correct(sudoku, 6, 6))
    final_row = row_check + column_check + block_check
    return all(final_row)

