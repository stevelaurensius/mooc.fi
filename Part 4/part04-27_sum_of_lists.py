# Please write a function named list_sum which takes two lists of integers as arguments.
# The function returns a new list which contains the sums of the items at each index in the
# two original lists. You may assume both lists have the same number of items.
# An example of the function at work:
# a = [1, 2, 3]
# b = [7, 8, 9]
# print(list_sum(a, b)) # [8, 10, 12]

def list_sum(x, y):
    return [x + y for x, y in zip(x, y)]


if __name__ == '__main__':
    a = [1, 2, 3]
    b = [4, 5, 12]
    print(list_sum(a, b))
