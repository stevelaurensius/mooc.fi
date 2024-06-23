# Please familiarize yourself with the Python module fractions. Use it to write a function
# named fractionate(amount: int), which takes the number of parts as its argument.
# The function should divide the number 1 into as many equal sized fractions as is specified
# by the argument, and return these in a list.
from fractions import Fraction


def fractionate(amount):
    return [Fraction(1, amount) for _ in range(amount)]
