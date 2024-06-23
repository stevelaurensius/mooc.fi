# Please write a function named double_items(numbers: list), which takes a list of
# integers as its argument.

# The function should return a new list, which contains all values from the original list
# doubled. The function should not change the original list.
def double_items(numbers: list):
    result = [x * 2 for x in numbers]
    return result


if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)
