# The Python string method isupper() returns True if a string consists of only
# uppercase characters.
def no_shouting(x):
    new_list = [i for i in x if i.isupper() == False]
    return new_list


if __name__ == '__main__':
    my_list = ['aaaa', 'BBBB', 'cccc', 'dddd', 'EEEE', 'ffff', 'GGGG']
    pruned_list = no_shouting(my_list)
    print(pruned_list)
