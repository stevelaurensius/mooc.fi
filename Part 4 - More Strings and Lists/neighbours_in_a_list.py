# Given a list of integers, let's decide that two consecutive items in the list are neighbours if
# their difference is 1. So, items 1 and 2 would be neighbours, and so would items 56 and 55.
#
# Please write a function named longest_series_of_neighbours, which looks for the
# longest series of neighbours within the list, and returns its length.
#
# For example, in the list [1, 2, 5, 4, 3, 4] the longest list of neighbours would be
# [5, 4, 3, 4], with a length of 4.
def longest_series_of_neighbours(my_list):
    counter = 1
    longest = 1
    for i in range(1, len(my_list)):
        if abs(my_list[i - 1] - my_list[i]) == 1:
            counter += 1
        else:
            counter = 1
        longest = max(longest, counter)
    return longest


if __name__ == '__main__':
    input_list = [1, 2, 5, 7, 6, 5, 6, 5, 3, 4, 1, 0]
    print(longest_series_of_neighbours(input_list))
