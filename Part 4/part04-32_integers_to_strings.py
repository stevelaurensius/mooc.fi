# Please write a function named formatted, which takes a list of floating point
# numbers as its argument. The function returns a new list, which contains each
# element of the original list in string format, rounded to two decimal points. The
# order of the items in the list should remain unchanged.
#
# An example of expected behaviour:
#
# my_list = [1.234, 0.3333, 0.11111, 3.446]
# new_list = formatted(my_list)
# print(new_list)
def formatted(input_list):
    x = [f'{i:.2f}' for i in input_list]
    return x


if __name__ == '__main__':
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list)
