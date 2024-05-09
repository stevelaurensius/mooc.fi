# In this exercise we will complete two more functions for the sudoku project from the
# previous section: print_sudoku and add_number.

# The function print_sudoku(sudoku: list) takes a two-dimensional array
# representing a sudoku grid as its argument. The function should print out the grid in the
# format specified in the examples below.

# The function add_number(sudoku: list, row_no: int, column_no: int,
# number:int) takes a two-dimensional array representing a sudoku grid, two integers
# referring to the row and column indexes of a single square, and a single digit between 1
# and 9, as its arguments. The function should add the digit to the specified location in the
# grid.
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
