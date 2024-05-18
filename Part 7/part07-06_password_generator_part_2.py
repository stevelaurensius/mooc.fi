# Please write an improved version of your password generator. The function now takes
# three arguments:

# - If the second argument is True, the generated password should also contain one or more numbers.
# - If the third argument is True, the generated password should also contain one or more of these
#   special characters: !?=+-()#.

# Despite these two additional arguments, the password should always contain at least one
# lowercase alphabet. You may assume the function will only be called with combinations of
# arguments that are possible to formulate into passwords following these rules. That is,
# the arguments will not specify e.g. a password of length 2 which contains both a number
# and a special characters, for then there would not be space for the mandatory lowercase
# letter.

import string
import random


def generate_strong_password(char_length: int, incl_number: bool, incl_special: bool):
    lowercase = string.ascii_lowercase
    numbers = string.digits
    special_char = '!?=+-()#'
    password = [random.choice(lowercase)]
    if incl_number:
        password.append(random.choice(numbers))
    if incl_special:
        password.append(random.choice(special_char))
    remaining_length = char_length - len(password)
    all_characters = lowercase
    if incl_number:
        all_characters += numbers
    if incl_special:
        all_characters += special_char
    if remaining_length > 0:
        password += random.choices(all_characters, k=remaining_length)
    random.shuffle(password)
    return ''.join(password)


if __name__ == '__main__':
    print(generate_strong_password(5, True, True))
