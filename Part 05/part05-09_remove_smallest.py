# Please write a function named remove_smallest(numbers: list), which takes a list
# of integers as its argument.

# The functions should find and remove the smallest item in the list. You may assume there
# is a single smallest item in the list.

# The function should not have a return value - it should directly modify the list it receives
# as a parameter.
def remove_smallest(numbers: list):
    if not numbers:
        return
    min_index = 0
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[min_index]:
            min_index = i
    numbers.pop(min_index)


if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)
