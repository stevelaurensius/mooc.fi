# Please write a function named line, which takes two arguments: an integer and a string.
# The function prints out a line of text, the length of which is specified by the first argument.
# The character used to draw the line should be the first character in the second argument.
# If the second argument is an empty string, the line should consist of stars.
#
# An example of expected behaviour:
#
# line(7, "%")
# line(10, "LOL")
# line(3, "")
#
# Sample output
# %%%%%%%
# LLLLLLLLLL
# ***

def line(x, y):
    if y == '':
        input_string = '*'
    else:
        input_string = y[0]
    print(input_string * x)


line(10, 'LOL')

