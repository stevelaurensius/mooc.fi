# Please write a function named length_of_longest, which takes a list of strings as its
# argument. The function returns the length of the longest string.
def length_of_longest(x):
    length = [len(i) for i in x]
    return max(length)


if __name__ == '__main__':
    my_list = ["first", "second", "fourth", "eleventh"]
    result = length_of_longest(my_list)
    print(result)
