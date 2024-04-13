# Please write a function named no_vowels, which takes a string argument. The
# function returns a new string, which should be the same as the original but with
# all vowels removed.

# You can assume the string will contain only characters from the lowercase
# English alphabet a...z.
def no_vowels(input_string):
    vowels = 'aiueo'
    final_string = ''
    for char in input_string:
        if char not in vowels:
            final_string += char
    return final_string


if __name__ == '__main__':
    my_string = "this is an example"
    print(no_vowels(my_string))
