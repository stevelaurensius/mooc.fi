# Please write a function named spruce, which takes one argument. The function prints
# out the text a spruce!, and a spruce tree, the size of which is specified by the
# argument.
def spruce(input_string):
    i = 1
    star_count = 1
    print('a spruce!')
    while i <= input_string:
        print(' ' * (input_string - i) + ('*' * star_count))
        i += 1
        star_count += 2
    i = 1
    star_count = 1
    print(' ' * (input_string - i) + ('*' * star_count))


if __name__ == "__main__":
    spruce(5)
