# Please write a function named range_of_list, which takes a list of integers as
# an argument. The function returns the difference between the smallest and the
# largest value in the list.
def range_of_list(x):
    x.sort()
    return x[-1] - x[0]


if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = range_of_list(my_list)
    print(result)
