# Please write a function named hypotenuse(leg1: float, leg2: float),
# which takes the lengths of the two sides adjacent to the right angle of an
# orthogonal triangle. The function should return the length of the hypotenuse, or
# the side opposite to the right angle.
import math


def hypotenuse(leg1: float, leg2: float):
    return math.sqrt(math.pow(leg1, 2) + math.pow(leg2, 2))
