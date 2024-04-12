# Please write a function named sum_of_positives, which takes a list of integers as its
# argument. The function returns the sum of the positive values in the list.
def sum_of_positives(x):
    positive_sum = 0
    for num in x:
        if num > 0:
            positive_sum += num
    return positive_sum


if __name__ == '__main__':
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)
