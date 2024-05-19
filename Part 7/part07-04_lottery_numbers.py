# Please write a function named lottery_numbers(amount: int, lower: int,
# upper: int), which generates as many random numbers as specified by the first
# argument. All numbers should fall within the bounds lower to upper. The numbers
# should be stored in a list and returned. The numbers should be in ascending order in the
# returned list.

# As these are lottery numbers, no number should appear twice in the list.
from random import sample


def lottery_numbers(samples: int, lower_range: int, upper_range: int):
    number_pool = list(range(lower_range, upper_range + 1))
    draw = sample(number_pool, samples)
    sorted_draw = sorted(draw)
    return sorted_draw
