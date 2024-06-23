# Please write a function named distinct_numbers, which takes a list of integers as its
# argument. The function returns a new list containing the numbers from the original list in
# order of magnitude, and so that each distinct number is present only once.
def distinct_numbers(x):
    unique_list = list(set(x))
    unique_list.sort()
    return unique_list


if __name__ == '__main__':
    my_list = [1000, 1, 10, 100, 100, 1]
    print(distinct_numbers(my_list))
