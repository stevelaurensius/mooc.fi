# Please write a function named everything_reversed, which takes a list of
# strings as its argument. The function returns a new list with all of the items on
# the original list reversed. Also the order of items should be reversed on the new
# list.
#
# An example of how the function should work:
# my_list = ["Hi", "there", "example", "one more"]
# new_list = everything_reversed(my_list)
# print(new_list)
def everything_reversed(x):
    return [i[::-1] for i in x[::-1]]


if __name__ == '__main__':
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)
