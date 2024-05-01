# Please write a function named count_matching_elements(my_matrix: list,
# element: int), which takes a two-dimensional array of integers and a single integer
# value as its arguments. The function then counts how many elements within the matrix
# match the argument value.

# An example of how the function should work:
# m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
# print(count_matching_elements(m, 1))

# Sample output
# 3

def count_matching_elements(my_matrix: list, element: int):
    counter = 0
    for set in my_matrix:
        for subset in set:
            if subset == element:
                counter += 1
    return counter


# print(count_matching_elements([[1, 2, 1], [0, 3, 4], [1, 0, 0]], 4))
