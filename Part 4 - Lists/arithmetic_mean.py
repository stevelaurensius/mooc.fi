# Please write a function named mean, which takes a list of integers as
# an argument. The function returns the arithmetic mean of the values in the list.
def mean(x):
    sum_of_numbers = 0
    for i in x:
        sum_of_numbers += i
    return sum_of_numbers / len(x)


if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)
