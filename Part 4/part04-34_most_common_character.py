# Please write a function named most_common_character, which takes a string
# argument. The function returns the character which has the most occurrences
# within the string. If there are many characters with equally many occurrences,
# the one which appears first in the string should be returned.
def most_common_character(x):
    most_common = x[0]
    for character in x:
        if x.count(character) > x.count(most_common):
            most_common = character
    return most_common


if __name__ == '__main__':
    second_string = "abcdbde"
    print(most_common_character(second_string))
