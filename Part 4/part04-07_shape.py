# Please write a function named shape, which takes four arguments. The first two
# parameters specify a triangle, as above, and the character used to draw it. The first
# parameter also specifies the width of a rectangle, while the third parameter specifies its
# height. The fourth parameter specifies the filler character of the rectangle. The function
# prints first the triangle, and then the rectangle below it.
#
# The function should call the function line from the exercise above for the actual printing
# out. Copy your solution to that exercise above the code for this exercise. Please don't
# change anything in the line function.
def line(x, y):
    if y == '':
        y = '*'
    print(y * x)


def shape(i, j, k, m):
    counter = 1
    while counter <= i:
        line(counter, j)
        counter += 1
    counter = 1
    while counter <= k:
        line(i, m)
        counter += 1


if __name__ == "__main__":
    shape(5, "x", 2, "o")
