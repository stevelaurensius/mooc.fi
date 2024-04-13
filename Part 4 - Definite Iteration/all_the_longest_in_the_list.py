# Please write a function named all_the_longest, which takes a list of strings as its
# argument. The function should return a new list containing the longest string in the
# original list. If more than one are equally long, the function should return all of the
# longest strings.
#
# The order of the strings in the returned list should be the same as in the original.
def all_the_longest(x):
    max_length = max(len(string) for string in x)
    new_list = [i for i in x if len(i) == max_length]
    return new_list


if __name__ == '__main__':
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']
