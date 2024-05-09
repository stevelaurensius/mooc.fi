# This is the very last sudoku task. This time we will create a slightly different version of the
# function for adding new numbers to the grid.

# The function copy_and_add(sudoku: list, row_no: int, column_no: int,
# number: int) takes a two-dimensional array representing a sudoku grid, two integers
# referring to the row and column indexes of a single square, and a single digit between 1
# and 9, as its arguments. The function should return a copy of the original grid with the
# new digit added in the correct location. The function should not change the original grid
# received as a parameter.

def print_sudoku(sudoku):
    for i in range(len(sudoku)):
        if i != 0 and i % 3 == 0:
            print()
        for j in range(len(sudoku[i])):
            if j != 0 and j % 3 == 0:
                print(" ", end="")
            if sudoku[i][j] == 0:
                print("_", end=" ")
            else:
                print(sudoku[i][j], end=" ")
        print()


def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number


def copy_and_add(sudoku: list, row_no: int, column_no: int, number:int):
    copied_sudoku = [row[:] for row in sudoku]
    copied_sudoku[row_no][column_no] = number
    return copied_sudoku
