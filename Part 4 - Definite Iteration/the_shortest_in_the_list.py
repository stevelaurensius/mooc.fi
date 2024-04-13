# Please write a function named shortest, which takes a list of strings as its argument.
# The function returns whichever of the strings is the shortest. If more than one are equally
# short, the function can return any of the shortest strings (there will be no such situation in
# the tests). You may assume there will be no empty strings in the list.
def shortest(x):
    short = min(x, key=len)
    return short


if __name__ == '__main__':
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = shortest(my_list)
    print(result)
