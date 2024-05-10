# Please write a function named histogram, which takes a string as its argument. The
# function should print out a histogram representing the number of times each letter
# occurs in the string. Each occurrence of a letter should be represented by a star on the
# specific line for that letter.

def histogram(input_string: str):
    result_dict = {}
    for i in input_string:
        if i not in result_dict:
            result_dict[i] = 0
        result_dict[i] += 1
    for i in result_dict:
        print(i, '*' * result_dict[i])
