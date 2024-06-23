# Please write a module named string_helper, which contains the following functions:

# The function change_case(orig_string: str) creates and returns a new version of
# the parameter string. The lowercase letters in the original should be uppercase, and
# uppercase letters should be lowercase.

# The function split_in_half(orig_string: str) splits the parameter string in half,
# and returns the results in a tuple. If the original has an odd number of characters, the first
# half should be shorter.

# The function remove_special_characters(orig_string: str) returns a new
# version of the parameter string, with all special characters removed. Only lowercase and
# uppercase letters, numbers and spaces are allowed in the returned string.
import string


def change_case(orig_string: str):
    result = ''
    for char in orig_string:
        if char.isupper():
            result += char.lower()
        elif char.islower():
            result += char.upper()
        else:
            result += char
    return result


def split_in_half(orig_string: str):
    half = (len(orig_string) / 2) - (len(orig_string) / 2 % 1)
    half = int(half)
    return (orig_string[:half], orig_string[half:])


def remove_special_characters(orig_string: str):
    control_list = ' '
    control_list += string.ascii_letters
    control_list += string.digits
    result = ''
    for char in orig_string:
        if char in control_list:
            result += char
    return result


if __name__ == '__main__':
    print(remove_special_characters("This is a test, lets see how it goes!!!11!"))
