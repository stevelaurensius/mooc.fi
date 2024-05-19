# Please write a function which creates passwords of a desired length, consisting of
# lowercase characters a to z.
import string
import random


def generate_password(char_length: int):
    characters = string.ascii_lowercase
    password = ''.join(random.choices(characters, k=char_length))
    return password
